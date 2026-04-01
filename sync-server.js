// Sync server: serves static files + WebSocket relay for live sync
// Usage: node sync-server.js
// Config: PORT env var (default 3000)

const http = require('http');
const fs = require('fs');
const path = require('path');
const { WebSocketServer } = require('ws');

const port = process.env.PORT || 3000;
const staticDir = __dirname;

const MIME = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
};

const server = http.createServer((req, res) => {
  let filePath = path.join(staticDir, decodeURIComponent(new URL(req.url, 'http://localhost').pathname));
  if (filePath.endsWith('/')) filePath += 'index.html';

  // Security: prevent directory traversal
  if (!filePath.startsWith(staticDir)) { res.writeHead(403); res.end(); return; }

  fs.readFile(filePath, (err, data) => {
    if (err) { res.writeHead(404); res.end('Not found'); return; }
    const ext = path.extname(filePath);
    res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
    res.end(data);
  });
});

// WebSocket on the same server
const wss = new WebSocketServer({ server, path: '/ws' });
const rooms = {};

wss.on('connection', (ws, req) => {
  const url = new URL(req.url, 'http://localhost');
  const room = url.searchParams.get('room') || 'default';

  if (!rooms[room]) rooms[room] = new Set();
  rooms[room].add(ws);
  console.log(`[${room}] +1 (${rooms[room].size} clients)`);

  ws.on('message', (data) => {
    for (const client of rooms[room]) {
      if (client !== ws && client.readyState === 1) {
        client.send(data.toString());
      }
    }
  });

  ws.on('close', () => {
    rooms[room].delete(ws);
    if (rooms[room].size === 0) delete rooms[room];
    console.log(`[${room}] -1 (${rooms[room]?.size || 0} clients)`);
  });
});

server.listen(port, () => {
  console.log(`Server running at http://0.0.0.0:${port}`);
});
