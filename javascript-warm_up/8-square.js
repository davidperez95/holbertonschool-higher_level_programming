#!/usr/bin/node
const process = require('process');

const args = process.argv;

const number = parseInt(args[2]);
const array = [];

for (let i = 0; i < number; i++) {
  array.push('X');
}
const sentence = array.join('');
for (let i = 0; i < number; i++) {
  console.log(sentence);
}
