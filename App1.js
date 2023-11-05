// app.js

/*const mathOps = require('./mathOperations'); // Import the module

console.log(`The value of pi is: ${mathOps.pi}`);
console.log(`3 + 4 = ${mathOps.add(3, 4)}`);
console.log(`5 * 6 = ${mathOps.multiply(5, 6)}`);*/


var http = require('http');
var dt = require('./mathOperations');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write("The date and time are currently: " + dt.myDateTime());
  res.end();
}).listen(8080);
