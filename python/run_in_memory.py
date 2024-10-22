import asyncio
from multiprocessing import Process, Queue

import receive_stream, send_image_stream

from queueue import q

def receiver(q):
    asyncio.run(receive_stream.main())

def server(q):
    send_image_stream.app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)

if __name__ == '__main__':

    receiver_process = Process(target=receiver, args=(q,))
    server_process = Process(target=server, args=(q,))

    # Start the processes
    receiver_process.start()
    server_process.start()

    # Join the processes
    receiver_process.join()
    server_process.join()