$(document).ready(function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    const translation = data.hello;
    $('#hello').append(translation);
  });
});
