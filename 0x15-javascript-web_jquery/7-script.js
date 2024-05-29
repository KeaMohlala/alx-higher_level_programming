const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$(document).ready(function () {
  $.get(URL, function (data) {
    const characterName = data.name;
    $('#character').text(characterName);
  });
});
