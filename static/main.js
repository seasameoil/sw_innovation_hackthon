let socket = new WebSocket('ws://localhost:8000/ws/graph/');

socket.onmessage = function(e) {
    var pageUrl = window.location.href;
    var last = pageUrl.substring(pageUrl.length-4);

    let djangoData = JSON.parse(e.data);
    console.log(djangoData);

    if (last == "main") {

        if (djangoData.fire == 'True') {
             document.getElementById('btn1').className = 'bus blink';
             document.getElementById('btn2').className = 'bus';
             document.getElementById('btn3').className = 'bus';
        // } else if (djangoData.count == true) {
            // document.getElementById('btn1').className = 'bus';
            // document.getElementById('btn2').className = 'bus blink';
            // document.getElementById('btn3').className = 'bus';
        } else if (djangoData.crime == 'ON') {
            document.getElementById('btn1').className = 'bus';
            document.getElementById('btn2').className = 'bus';
            document.getElementById('btn3').className = 'bus blink';
        }

        document.getElementById('count').innerHTML = djangoData.count;
    }
}
