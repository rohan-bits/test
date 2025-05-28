import asyncio
import websockets

async def handle_client(websocket, path):
    print("Client connected!")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            await websocket.send(f"Echo: {message}")  # Send response back
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    server = await websockets.serve(handle_client, "localhost", 8080)
    await server.wait_closed()

asyncio.run(main())
