#!/usr/bin/node

const i = require('i');
const file = process.argv[2];

i.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
