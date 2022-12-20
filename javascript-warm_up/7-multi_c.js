#!/usr/bin/node
const process = require('process');

const args = process.argv;

const number = parseInt(args[2]);

if (isNaN(number) === false) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
