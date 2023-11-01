let socket = new WebSocket('ws://localhost:8000/ws/graph/');

socket.onmessage = function(e) {
    let djangoData = JSON.parse(e.data);
    console.log(djangoData);

    document.querySelector('#hour').innerHTML = djangoData.hour;

    if (last == "bus2") {
        document.querySelector('#total2').innerHTML = djangoData.value2;
        document.querySelector('#value2').innerHTML = djangoData.cong2;
        if (cong2 == "여유") {
            document.querySelector('#value2').style = "green";
        }
        else if (cong2 == "보통") {
            document.querySelector('#value2').style = "blue";
        }
        else if (cong2 == "혼잡") {
            document.querySelector('#value2').style = "yellow";
        }
        else {
            document.querySelector('#value2').style = "red";
        }
    } else {
        document.querySelector('#total1').innerHTML = djangoData.value1;
        document.querySelector('#value1').innerHTML = djangoData.cong1;
        if (cong1 == "여유") {
            document.querySelector('#value1').style = "green";
        }
        else if (cong1 == "보통") {
            document.querySelector('#value1').style = "blue";
        }
        else if (cong1 == "혼잡") {
            document.querySelector('#value1').style = "yellow";
        }
        else {
            document.querySelector('#value1').style = "red";
        }
    }
}
