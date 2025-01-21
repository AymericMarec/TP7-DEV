import asyncio
import websockets

async def hello(websocket):
    message = await websocket.recv()
    print(f"<<< {message}")
    greeting = f"Hello client ! Received {message}"
    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main():
    async with websockets.serve(hello, "localhost", 8000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
