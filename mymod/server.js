// Import the http module
const http = require('http');
const hostname = '127.0.0.1';
const port = 4000;

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.statusCode = 200; // OK

  res.end('This is Node.js HTTP Server\n');
});
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
