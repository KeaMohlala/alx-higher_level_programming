#!/usr/bin/node

const { argv } = process;
const numArgs = argv.length - 2;

if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
