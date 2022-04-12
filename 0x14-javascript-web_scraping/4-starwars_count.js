#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const json = JSON.parse(body);
    json.results.forEach((i) => {
      if (i.characters.indexOf('https://swapi-api.hbtn.io/api/people/18/') !== -1) count++;
    });
    console.log(count);
  }
});
