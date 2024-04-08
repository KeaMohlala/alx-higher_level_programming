#!/usr/bin/node

const { argv } = process;
const first = argv[2];

if (!first) {
  console.log('No argument');
} else {
  console.log(first);
}
