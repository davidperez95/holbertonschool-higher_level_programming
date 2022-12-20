#!/usr/bin/node
const process = require('process');

const args = process.argv;
const length = args.length;

if (length === 2) {
  console.log('No argument');
} else if (length === 3) {
  console.log('Argument found');
} else if (length > 3) {
  console.log('Arguments found');
}
