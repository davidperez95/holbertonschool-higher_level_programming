#!/usr/bin/node

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    super.print(c)
  }
};
