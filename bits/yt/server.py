import asyncio
import websockets
from websockets.asyncio.server import serve

async def hello(websocket):
    name = await websocket.recv()
    print(f'Server Received: {name}')
    greeting = f' Hello {name}!'
    
    await websocket.send(greeting)
    print(f'Server Sent: {greeting}')
    
async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()