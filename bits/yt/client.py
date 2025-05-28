import asyncio
import websockets
import websockets.asyncio.client

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as ws:
        name = input("What's your name?")
        
        greeting = await ws.recv()
        print("Client receoved: {greeting}")
        
if __name__ == "__main__":
    asyncio.run(hello())