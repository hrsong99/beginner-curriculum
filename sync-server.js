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
  const url = new URL(req.url, 'http://localhost');

  // Health check / WS status endpoint
  if (url.pathname === '/ws') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    const roomInfo = {};
    for (const [name, clients] of Object.entries(rooms)) roomInfo[name] = clients.size;
    res.end(JSON.stringify({ status: 'ok', rooms: roomInfo }));
    return;
  }

  let filePath = path.join(staticDir, decodeURIComponent(url.pathname));
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

// WebSocket — handle upgrade manually (more reliable behind reverse proxies)
const wss = new WebSocketServer({ noServer: true });
const rooms = {};

server.on('upgrade', (req, socket, head) => {
  const url = new URL(req.url, 'http://localhost');
  if (url.pathname !== '/ws') {
    socket.destroy();
    return;
  }
  wss.handleUpgrade(req, socket, head, (ws) => {
    wss.emit('connection', ws, req);
  });
});

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
