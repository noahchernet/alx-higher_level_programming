#!/usr/bin/node
const argv = require('process').argv;

if (argv.length >= 3) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
