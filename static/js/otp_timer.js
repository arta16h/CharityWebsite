let timerOn = false;
function timer(remaining, showCountDiv) {
    var m = Math.floor(remaining / 60);
    var s = remaining % 60;
    
    m = m < 10 ? '0' + m : m;
    s = s < 10 ? '0' + s : s;
    showCountDiv.innerHTML = m + ':' + s;
    remaining -= 1;
    
    if(remaining >= 0 && timerOn) {
        setTimeout(function() {
            timer(remaining, showCountDiv);
        }, 1000);
        return;
    }

    if(!timerOn) {
        // Do validate stuff here
        return;
    }
    timerOn = false
    // Do timeout stuff here
}