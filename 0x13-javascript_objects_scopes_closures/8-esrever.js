#!/usr/bin/node

exports.esrever = function (list) {
  const listLength = list.length;
  const newList = [];
  let i = listLength - 1;
  while (i >= 0) {
    newList.push(list[i]);
    i--;
  }
  return newList;
};
