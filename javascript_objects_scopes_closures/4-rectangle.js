#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (char = 'X') {
    const array = [];
    for (let i = 0; i < this.width; i++) {
      array.push(char);
    }
    const setense = array.join('');
    for (let i = 0; i < this.height; i++) {
      console.log(setense);
    }
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
