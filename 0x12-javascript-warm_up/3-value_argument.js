#!/usr/bin/node
const arg = process.argv;
console.log(arg[2] === undefined ? 'No argument' : process.argv[2]);
