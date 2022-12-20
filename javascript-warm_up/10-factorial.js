#!/usr/bin/node
const process = require('process');
const args = process.argv;
let number = parseInt(args[2]);

if (isNaN(number) === true) {
  number = 1;
}

function factorial (n) {
  // base case
  if (n === 0 || n === 1) {
    return 1;
    // recursive case
  } else {
    return n * factorial(n - 1);
  }
}

const answer = factorial(number);
console.log(answer);
