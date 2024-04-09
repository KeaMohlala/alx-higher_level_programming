#!/usr/bin/node

function factorial (n) {
  if (n === 0) {
    return 1;
  } else if (n > 0) {
    return (n * factorial(n - 1));
  } else {
    return -1;
  }
}
const { argv } = process;
const first = parseInt(argv[2], 10);

if (isNaN(first)) {
  console.log('1');
} else {
  console.log(factorial(first));
}
