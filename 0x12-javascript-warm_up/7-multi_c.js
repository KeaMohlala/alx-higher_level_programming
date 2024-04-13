#!/usr/bin/node

const { argv } = process;
const first = argv[2];
const intValue = parseInt(first, 10);

if (isNaN(intValue)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < intValue) {
    console.log('C is fun');
    i++;
  }
}
