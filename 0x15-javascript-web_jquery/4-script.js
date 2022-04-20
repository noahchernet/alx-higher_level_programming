// Toggles the header's color when the 'red header' text is clicked on
// by setting the header's class to red
$(document).ready(function () {
  $('#toggle_header').on('click', function () {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else {
      $('header').removeClass('red');
      $('header').addClass('green');
    }
  });
});
