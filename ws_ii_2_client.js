console.log("test")

let input_pseudo = document.getElementById("input-pseudo")
let input_message = document.getElementById("input-message")

let pseudo_div = document.getElementById("pseudo-selector")
let chatbox = document.getElementById("chatbox")
let chat = document.getElementById("chat")

let pseudo = ""

const ws = new WebSocket("ws://10.1.1.253:8000");
  
ws.onmessage = (event) => {
    console.log(event.data)
    console.log(event.data.slice(0,9))
    console.log(event.data.slice(0,3))
    if(event.data.slice(0,9) == "connect|"){
        console.log("connecté !")
        pseudo_div.style.display = "none"
        chatbox.style.display = "block"
        pseudo = event.data.slice(8,event.data.length)
    }else if(event.data.slice(0,3) == "id|"){
        id =  event.data.slice(3,event.data.length)
        pseudo_div.style.display = "none"
        chatbox.style.display = "block"
        localStorage.setItem("id", id);
    }else {
        console.log("Message recu :",event.data);
        const msg = document.createElement("p");
        msg.textContent = event.data
        chat.appendChild(msg)};
    }

ws.onopen = (event) =>{
    console.log("Connecté en websocket !")
    const client_id = localStorage.getItem("id");
    console.log(client_id)
    if(client_id != null){
        ws.send(client_id)
    }else{
        ws.send("new")
    }
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


