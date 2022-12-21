#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    const array = [];
    for (let i = 0; i < this.size; i++) {
      array.push(c);
    }

    const sentence = array.join('');
    for (let i = 0; i < this.size; i++) {
      console.log(sentence);
    }
  }
};
