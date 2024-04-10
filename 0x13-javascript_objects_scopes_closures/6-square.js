#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      let i = 0;
      while (i < this.size) {
        let row = '';
        let j = 0;
        while (j < this.size) {
          row += 'X';
          j++;
        }
        i++;
        console.log(row.trim());
      }
    } else {
      let i = 0;
      while (i < this.size) {
        let row = '';
        let j = 0;
        while (j < this.size) {
          row += c;
          j++;
        }
        i++;
        console.log(row.trim());
      }
    }
  }
}
module.exports = Square;
