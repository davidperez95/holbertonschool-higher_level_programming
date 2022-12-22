#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterURL = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, function (error, response, body) {
  if (error) console.log(error);
  const bodyObj = JSON.parse(body);
  const resultsLength = bodyObj.results.length;
  let counter = 0;

  for (let i = 0; i < resultsLength; i++) {
    if (bodyObj.results[i].characters.includes(characterURL) === true) {
      counter += 1;
    }
  }

  console.log(counter);
});
