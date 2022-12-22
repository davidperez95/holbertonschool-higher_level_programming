#!/usr/bin/node

const request = require('request');
const filmID = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmID}`;

request(url, function (error, response, body) {
  if (error) console.log(error);
  const bodyObj = JSON.parse(body);

  console.log(bodyObj.title);
});
