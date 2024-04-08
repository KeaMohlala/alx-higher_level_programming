#!/usr/bin/node

const { argv } = process;
const first = argv[2];
const intValue = parseInt(first, 10);

if (isNaN(intValue)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${intValue}`);
}
