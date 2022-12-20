#!/usr/bin/node
const process = require('process');

const args = process.argv;

const number = parseInt(args[2]);
if (isNaN(number) === true) {
  console.log('Missing size');
}

const array = [];
for (let i = 0; i < number; i++) {
  array.push('X');
}
const sentence = array.join('');
for (let i = 0; i < number; i++) {
  console.log(sentence);
}
