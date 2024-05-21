#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error);
    return;
  }
  const movieTitle = JSON.parse(body).title;
  console.log(movieTitle);
});
