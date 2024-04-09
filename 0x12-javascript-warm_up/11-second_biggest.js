#!/usr/bin/node

function SecondLargest (arr) {
  let firstMax = -Infinity;
  let secondMax = -Infinity;

  for (const num of arr) {
    if (num > firstMax) {
      secondMax = firstMax;
      firstMax = num;
    } else if (num > secondMax && num !== firstMax) {
      secondMax = num;
    }
  }
  return secondMax;
}

const { argv } = process;
const numArgs = argv.length;

if (numArgs <= 3) {
  console.log('0');
} else {
  console.log(SecondLargest(argv));
}
