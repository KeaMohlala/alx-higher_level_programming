#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const filePath = process.argv[3];
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error);
    return;
  }

  fs.writeFile(filePath, body, 'utf8', function (err) {
    if (err) {
      console.error('Error writing file:', err);
    }
  });
});
