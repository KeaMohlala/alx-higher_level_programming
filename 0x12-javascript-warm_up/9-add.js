#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const { argv } = process;
const first = parseInt(argv[2], 10);
const second = parseInt(argv[3], 10);

if (isNaN(first) || isNaN(second)) {
  console.log('NaN');
} else {
  console.log(add(first, second));
}
