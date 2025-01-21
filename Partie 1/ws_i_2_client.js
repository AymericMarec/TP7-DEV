console.log("test")

let text = document.getElementById("input")

const ws = new WebSocket("ws://localhost:8000");
  
ws.onmessage = (event) => {
    console.log(event.data);
};

//relié avec un bouton qui envoie donc l'input au serveur
function sendmessage(){
    ws.send(text.value);
}


