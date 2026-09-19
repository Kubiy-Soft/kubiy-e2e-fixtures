const http = require('http');
const PORT = process.env.PORT || process.env.APP_PORT || 3000;
const VERSION = 'v1', BRANCH = 'node';
const s = http.createServer((req, res) => {
  if (req.url === '/health' || req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok', runtime: 'node', source: 'github', version: VERSION, branch: BRANCH }));
    return;
  }
  res.writeHead(404); res.end('not found');
});
s.listen(PORT, '0.0.0.0', () => console.log('gh node ' + VERSION + ' branch=' + BRANCH + ' on ' + PORT));
