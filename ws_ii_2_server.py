import asyncio
import websockets
import redis.asyncio as redis
import uuid

async def Client(websocket):
    global Clients
    Clients.append(websocket)
    print("new client")
    id = await websocket.recv()
    
    if(await client.get('id') == id):
        pseudo = await client.get(id)
        await websocket.send("connect|"+pseudo)
        print("hop")
    else :
        await CreateUser(websocket)        

    while True:
        message = await websocket.recv()
        await broadcast_messages(message)
        print(f"Message recu {message}")

async def broadcast_messages(message):
    global Clients
    for client in Clients:
        print(f"message envoyé en broadcast a {client}")
        await client.send(message)

async def CreateUser(websocket):
    global client
    id = str(uuid.uuid4())
    print("create id : "+id)
    pseudo = await websocket.recv()
    print(f"{pseudo} a rejoint !")
    await client.set(id, pseudo)
    await websocket.send("id|"+id)

async def main():
    async with websockets.serve(Client, "10.1.1.253", 8000):
        await asyncio.Future()  # run forever

Clients = []

if __name__ == "__main__":
    client = redis.Redis(host="10.1.1.253", port=6379)
    asyncio.run(main())
