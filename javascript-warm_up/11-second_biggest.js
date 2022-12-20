#!/usr/bin/node
const process = require('process');
const args = process.argv;
const argsLength = args.length;
const numbers = [];

for (let i = 2; i < argsLength; i++) {
  const newNumber = parseInt(args[i]);
  numbers.push(newNumber);
}

numbers.sort(function (a, b) {
  return (a - b);
});

if (numbers.length === 0 || numbers.length === 1) {
  console.log(0);
} else {
  console.log(numbers[numbers.length - 2]);
}
