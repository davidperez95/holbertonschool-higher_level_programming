#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let times = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      times += 1;
    }
  }
  return times;
};
