const fs = require('fs');
const filePath = 'input.txt';
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
  } else {
    console.log('File Contents:');
    console.log(data);
  }
});
