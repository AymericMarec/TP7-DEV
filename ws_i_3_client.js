console.log("test")

let input_pseudo = document.getElementById("input-pseudo")
let input_message = document.getElementById("input-message")

let pseudo_div = document.getElementById("pseudo-selector")
let chatbox = document.getElementById("chatbox")
let chat = document.getElementById("chat")

let pseudo = ""

const ws = new WebSocket("ws://localhost:8000");
  
ws.onmessage = (event) => {
    console.log("Message recu :",event.data);
    const msg = document.createElement("p");
    msg.textContent = event.data
    chat.appendChild(msg)};

ws.onopen = (event) =>{
    console.log("Connecté en websocket !")
}

ws.onclose = (event) =>{
    console.log("Deconexion ...")
}

function sendmessage(){
    ws.send(pseudo + " : " +input_message.value);
    input_message.value =""
}

function sendpseudo(){
    ws.send(input_pseudo.value);
    pseudo = input_pseudo.value
    pseudo_div.style.display = "none"
    chatbox.style.display = "block"
}


