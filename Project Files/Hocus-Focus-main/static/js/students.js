$(".content").hide();
document.addEventListener('DOMContentLoaded', function() {
  const webSocketBridge = new channels.WebSocketBridge();
  webSocketBridge.connect('/ws/');
  webSocketBridge.listen(function(action, stream) {
    if(action.type=="start"){
      if(action.token=="Yes"){
        $('#what').text("Are you listening to the class?");
      }else{
        $('#what').text("What did the teacher teach?");
      }
      $('#question').text("Question "+action.qno);
      $('#token').val(action.token);
      $(".content").slideToggle();
      for(var i=0;i<4;i++){
        $('#flexRadioDefault'+i).val(action.options[i]);
        $('#label'+i).html(action.options[i]);
      }
      setTimeout(function (){
        if($('#token').val()==$("input:radio[name=chosenoption]:checked").val()){
          var score=$("#score").text();
          $("#score").text(parseInt(score)+1);
        }
        $(".content").slideToggle();
      },5000);
    }else{
      alert("Score "+$("#score").text());
    }
  }
)
  document.ws = webSocketBridge; /* for debugging */
});
