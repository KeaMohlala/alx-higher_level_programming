const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.get(URL, function (data) {
    const translation = data.hello;
    $('#hello').text(translation);
  });
});
