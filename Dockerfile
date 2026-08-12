FROM nginx:alpine

# This repository is a static site. Live lesson state is provided by
# Lemonboard, so the retired Japanese WebSocket server is not included.
COPY index.html /usr/share/nginx/html/index.html
COPY viewer.html /usr/share/nginx/html/viewer.html
COPY ux-philosophy.md /usr/share/nginx/html/ux-philosophy.md
# Shared by every curriculum, so it lives at the root rather than in one
# language's folder. Every deck loads it — miss this COPY and the whole site
# renders unstyled with nothing in the console to say why.
COPY runtime/ /usr/share/nginx/html/runtime/
COPY english/ /usr/share/nginx/html/english/
COPY korean/ /usr/share/nginx/html/korean/
COPY _archive/ /usr/share/nginx/html/_archive/

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --quiet --spider http://127.0.0.1/ || exit 1
