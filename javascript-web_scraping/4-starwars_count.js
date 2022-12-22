#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let counter = 0;

request(url, function (error, response, body) {
  if (error) console.log(error);
  // store the json list of objects on bodyObj
  const bodyObj = JSON.parse(body).results;
  // iterate on each object in the list
  for (let i = 0; i < bodyObj.length; i++) {
    // assing the list of characters to charactersList
    const charactersList = bodyObj[i].characters;
    // iterate on each character list
    for (let j = 0; j < charactersList.length; j++) {
      // split the url string to find the last number and
      // assign it to character ID
      const characterID = charactersList[j].split('/')[5];
      if (characterID === '18') {
        counter += 1;
      }
    }
  }

  console.log(counter);
});
