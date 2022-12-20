#!/usr/bin/node
const process = require('process');

const args = process.argv;

let length = 0;

while (args[length] !== undefined) {
  length++;
}

if (length > 2) {
  for (let i = 2; i < length; i++) {
    console.log(args[i]);
  }
} else {
  console.log('No argument');
}
