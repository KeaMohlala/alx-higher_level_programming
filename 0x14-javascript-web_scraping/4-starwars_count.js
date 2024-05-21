#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

let wedgeCount = 0;
const wedgeId = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error);
    return;
  }

  const films = JSON.parse(body);
  films.results.forEach(film => {
    film.characters.forEach(characterId => {
      if (characterId === wedgeId) {
        wedgeCount++;
      }
    });
  });

  console.log(wedgeCount);
});
