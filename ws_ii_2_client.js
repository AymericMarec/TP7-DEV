let input_pseudo = document.getElementById("input-pseudo")
let input_message = document.getElementById("input-message")

let pseudo_div = document.getElementById("pseudo-selector")
let chatbox = document.getElementById("chatbox")
let chat = document.getElementById("chat")
let pseudotittle = document.getElementById("pseudoTittle")

let pseudo = ""
let id = ""

const ws = new WebSocket("ws://10.1.1.253:8000");
  
ws.onmessage = (event) => {
    if(event.data.slice(0,8) == "connect|"){
        console.log("connecté !")
        pseudo_div.style.display = "none"
        chatbox.style.display = "block"
        pseudo = event.data.slice(8,event.data.length)
        pseudotittle.innerText = "connecté en tant que : "+pseudo
    }else if(event.data.slice(0,3) == "id|"){
        id =  event.data.slice(3,event.data.length)
        pseudo_div.style.display = "none"
        chatbox.style.display = "block"
        localStorage.setItem("id", id);
        pseudotittle.innerText = "connecté en tant que : "+pseudo
    }else {
        console.log("Message recu :",event.data);
        const msg = document.createElement("p");
        msg.textContent = event.data
        chat.appendChild(msg)};
    }

ws.onopen = (event) =>{
    console.log("Connecté en websocket !")
    const client_id = localStorage.getItem("id");
    if(client_id != null){
        ws.send(client_id)
    }else{
        id = client_id
        ws.send("new")
    }
}

ws.onclose = (event) =>{
    console.log("Deconexion ...")
}

function sendmessage(){
    console.log("envoie : ",input_message.value)
    ws.send(input_message.value);
    input_message.value =""
}


function sendpseudo(){
    ws.send(input_pseudo.value);
    pseudo = input_pseudo.value
    pseudo_div.style.display = "none"
    chatbox.style.display = "block"
}


