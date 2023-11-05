// mymodule/app.js
const mymodule = require('./mymod');
console.log(`The value of pi is: ${mymodule.pi}`);
console.log(`3 + 4 = ${mymodule.add(10, 40)}`);
console.log(`5 - 2 = ${mymodule.subtract(50, 60)}`);
console.log(`5 - 2 = ${mymodule.mod(5, 10)}`);