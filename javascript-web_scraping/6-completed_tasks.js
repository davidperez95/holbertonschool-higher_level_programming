#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) console.log(error);
  const bodyObj = JSON.parse(body);
  const newObj = {};

  for (let i = 0; i < bodyObj.length; i++) {
    const userId = bodyObj[i].userId;
    const completed = bodyObj[i].completed;

    if (completed === true && !newObj[userId]) {
      newObj[userId] = 0;
    }

    if (completed === true) {
      newObj[userId] += 1;
    }
  }
  console.log(newObj);
});
