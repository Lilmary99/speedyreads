function pageScroll(increment) {
    var end = (document.getElementById('scroll_container').scrollHeight-document.getElementById('scroll_container').offsetHeight) ;
   if(document.getElementById('scroll_container').scrollTop < end){
         document.getElementById('scroll_container').scrollTop=document.getElementById('scroll_container').scrollTop+increment
         }

   scrolldelay = setTimeout("pageScroll(2.5)",100);
}
function stopScroll() {
    	clearTimeout(scrolldelay);
}
globalMinutes = 0;
globalSeconds = 0;
function constructTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        globalSeconds = seconds
        globalMinutes = minutes

        display.textContent = minutes + ":" + seconds;
        if (++timer < 0) {
            timer = duration;
        }
    }, 1000);
}

function startTime() {
  var zeroTime = 0;
  display = document.querySelector('#time');
  constructTimer(zeroTime, display);
}

$('#start').click(function () {
  var zeroTime = 0;
  display = document.querySelector('#time');
  constructTimer(zeroTime, display);
});

function getWPM() {
  minutes = globalMinutes/1 + (globalSeconds/60.0)
  wpm = 857.0 / minutes
  alert("You read "+ wpm + " words per minute")
}

function evalAnswer() {
    /*alert("I work!!!");*/
    if($('#correct').is(':checked'))
    {
        answeredCorrect();
        pageScroll();
    }
    else {
         $("#scroll_container").scrollTop(0);
     }
}

function answeredCorrect(){
    $('.section1').addClass("hidden");
    $('.section2').removeClass("hidden")
}
