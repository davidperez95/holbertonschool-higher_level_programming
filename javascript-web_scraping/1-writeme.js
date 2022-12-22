#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const stringToSave = process.argv[3];

fs.writeFile(filePath, stringToSave, function (error) {
  if (error) {
    throw error;
  }
  console.log('Saved!');
});
