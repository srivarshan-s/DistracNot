function startdn(formdata) {
  event.preventDefault();
  $('#start').prop('disabled', true);
  $("#start").css("background-color", "black");
  $('#stop').prop('disabled', false);
  $("#stop").css("background-color", '#2c2c2c');
  $.ajax({
    type:"POST",
    url:"http://127.0.0.1:8000/start",
    data:  {
      course: formdata['course'].value,
      lang: formdata['lang'].value,
      },
    success: function(data){}
  });
}

function stopdn(formdata) {
  event.preventDefault();
  $('#stop').prop('disabled', true);
  $("#stop").css("background-color", "black");
  $('#start').prop('disabled', false);
  $("#start").css("background-color", '#2c2c2c');
  $.ajax({
    type:"POST",
    url:"http://127.0.0.1:8000/stop",
    data:  {
        course: formdata['course'].value,
      },
    success: function(data){
  }
  });
}
