import asyncio
import websockets
import binascii
from io import BytesIO

from PIL import Image, UnidentifiedImageError

def is_valid_image(image_bytes):
    try:
        Image.open(BytesIO(image_bytes))
        # print("image OK")
        return True
    except UnidentifiedImageError:
        print("image invalid")
        return False

async def handle_connection(websocket, path):
    while True:
        try:
            message = await websocket.recv()
            print(len(message))
            if len(message) > 5000:
                  if is_valid_image(message):
                          #print(message)
                          with open("image.jpg", "wb") as f:
                                f.write(message)

            print()
        except websockets.exceptions.ConnectionClosed:
            break

async def main():
    server = await websockets.serve(handle_connection, '0.0.0.0', 3001)
    await server.wait_closed()

asyncio.run(main())
