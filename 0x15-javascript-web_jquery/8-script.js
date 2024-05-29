$(document).ready(function () {
  const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(URL, function (data) {
    // Iterate over each film in the data array
    data.results.forEach(function (film) {
      // Create a new <li> element for each film
      const listItem = $('<li></li>').text(film.title);
      $('#list_movies').append(listItem);
    });
  });
});
