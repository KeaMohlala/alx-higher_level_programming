#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // create empty object
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      let row = '';
      let j = 0;
      while (j < this.width) {
        row += 'X';
        j++;
      }
      i++;
      console.log(row.trim());
    }
  }
}
module.exports = Rectangle;
