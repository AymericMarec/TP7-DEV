import asyncio
import websockets

async def Client(websocket):
    global Clients
    Clients.append(websocket)
    print("new client")
    pseudo = await websocket.recv()
    print(f"{pseudo} a rejoint !")
    while True:
        message = await websocket.recv()
        await broadcast_messages(message)
        print(f"Message recu {message}")

async def broadcast_messages(message):
    global Clients
    for client in Clients:
        print(f"message envoyé en broadcast a {client}")
        await client.send(message)

async def main():
    async with websockets.serve(Client, "localhost", 8000):
        await asyncio.Future()  # run forever

Clients = []

if __name__ == "__main__":
    asyncio.run(main())
