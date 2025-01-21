import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        message = input("Envoie un message")

        await websocket.send(message)
        print(f">>> {message}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())
