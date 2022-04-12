#!/usr/bin/node
// Writes string to a file

const filename = process.argv[2];
const text = process.argv[3];
// console.log(filename)
const fs = require('fs');

fs.writeFile(filename, text, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
