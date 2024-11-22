import asyncio
import websockets
import redis.asyncio as redis
import uuid

async def Client(websocket):
    global Clients
    global client
    Clients.append(websocket)
    print("new client")
    try :
        id = await websocket.recv()
        pseudo = await client.get(id)
        if(id == "new" or pseudo is None):
            print("Nouvel utilisateur")
            await CreateUser(websocket)
        else :
            print(f"{pseudo} vient de se reconnecter !")
            await websocket.send("connect|"+str(pseudo)[2:len(pseudo)-1])     

        while True:
            message = await websocket.recv()
            await broadcast_messages(message)
            print(f"Message recu {message}")
    except:
        Clients.remove(websocket)
        print("un client s'est deconnecté")

async def broadcast_messages(message):
    global Clients
    for client in Clients:
        try:
            await client.send(message)
        except:
            Clients.remove(client)
            print("deconnecté")   

async def CreateUser(websocket):
    global client
    id = str(uuid.uuid4())
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
