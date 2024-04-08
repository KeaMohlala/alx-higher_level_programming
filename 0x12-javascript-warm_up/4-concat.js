#!/usr/bin/node

const { argv } = process;
const first = argv[2];
const second = argv[3];

if (!second) {
  console.log(first + ' is ' + undefined);
} else if (!second && !first) {
  console.log(undefined + ' is ' + undefined);
} else {
  console.log(first + ' is ' + second);
}
