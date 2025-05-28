import asyncio
import websockets
async def client():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, Server!")
        response = await websocket.recv()
        print(f"Received from server: {response}")
        
asyncio.run(client())