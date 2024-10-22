import asyncio
import websockets
import binascii
from io import BytesIO

from PIL import Image, UnidentifiedImageError

from multiprocessing import Queue

from queueue import q

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
            #print(len(message)) # This made the IP to connect to go away
            if len(message) > 5000:
                  if is_valid_image(message):
                          #print(message)
                          q.put(message) # puts message into queue

            #print()
        except websockets.exceptions.ConnectionClosed:
            break

async def main():
    server = await websockets.serve(handle_connection, '0.0.0.0', 3001)
    await server.wait_closed()
