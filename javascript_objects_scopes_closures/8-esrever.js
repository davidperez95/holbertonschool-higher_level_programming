#!/usr/bin/node

exports.esrever = function (list) {
  const newArray = [];
  let lastPosition = list.length - 1;

  for (; lastPosition >= 0; lastPosition--) {
    newArray.push(list[lastPosition]);
  }

  return newArray;
};
