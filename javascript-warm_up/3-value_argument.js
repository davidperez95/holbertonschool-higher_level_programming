#!/usr/bin/node
const process = require('process');

const args = process.argv;

let length = 0;

while (args[length] !== undefined) {
  length++;
}

if (length >= 2) {
  console.log(args[2])
} else {
  console.log('No argument')
}
