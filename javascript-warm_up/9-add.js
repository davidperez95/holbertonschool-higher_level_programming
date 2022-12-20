#!/usr/bin/node
const process = require('process');

const args = process.argv;
const intOne = parseInt(args[2]);
const intTwo = parseInt(args[3]);

function add (a, b) {
  console.log(a + b);
}

add(intOne, intTwo);
