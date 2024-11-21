import asyncio
import websockets
import redis.asyncio as redis
import json

async def Client(websocket):
    global Clients
    global clientDB
    print("new client")
    pseudo = await websocket.recv()
    Clients.append(pseudo)
    await clientDB.set(pseudo, json.dumps(websocket))
    print(f"{pseudo} a rejoint !")
    while True:
        message = await websocket.recv()
        await broadcast_messages(message)
        print(f"Message recu {message}")

async def broadcast_messages(message):
    global Clients
    for client in Clients:
        ws_client =  json.loads(client.get(client))
        print(f"message envoyé en broadcast a {client}")
        await ws_client.send(message)

async def main():
    async with websockets.serve(Client, "10.1.1.253", 8000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    Clients = []
    clientDB = redis.Redis(host="10.1.1.253", port=6379)
    asyncio.run(main())
