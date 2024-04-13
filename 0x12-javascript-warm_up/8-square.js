#!/usr/bin/node

const { argv } = process;
const first = argv[2];
const intValue = parseInt(first, 10);

if (isNaN(intValue)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < intValue) {
    let row = '';
    let j = 0;
    while (j < intValue) {
      row += 'X';
      j++;
    }
    i++;
    console.log(row.trim());
  }
}
