$(function() {
  var id = $('body').attr('id');
  $('ul li #' + id).parent().addClass('active');
});
