const os = require('os');
const path = require('path');
const fs = require('fs');

console.log('Operating System Information:');
console.log('Platform: ' + os.platform());
console.log('Architecture: ' + os.arch());
console.log('Total Memory: ' + (os.totalmem() / (1024 * 1024 * 1024) + ' GB'));
console.log('Free Memory: ' + (os.freemem() / (1024 * 1024 * 1024) + ' GB'));

const filePath = path.join(__dirname, 'sample.txt');
const fileContent = 'This is a sample text file created using Node.js built-in modules.';

fs.writeFile(filePath, fileContent, (err) => {
  if (err) {
    console.error('Error writing to file:', err);
  } else {
    console.log('File created and written successfully.');
  }
});

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
  } else {
    console.log('File Contents:');
    console.log(data);
  }
});
