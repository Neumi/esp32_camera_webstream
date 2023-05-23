![headline](/images/headline.jpg)


# esp32_camera_webstream
Bringing the ESP32 camera video stream to the web!


The Arduino ESP32-Camera test sketch only lets you use the stream on your local network. To get the stream to the web, you need a bit more...

This collection of scripts consists of:
 - Arduino code for ESP32 camera module (AI Thinker CAM) `websocket_camera_stream.ino`
 - Python code to receive the images via websockets with `receive_stream.py`
 - Python code to push the most recent image to a website with `send_image_stream.py`


 # Why is this cool?
I havent found a working repository that streams ESP32 camera images in real time to a web backend. This sovles this issue.

# How to run?
1. Open the ESP32 code in your Arduino IDE, install all missing libraries, change the `ssid`, `password` and `websockets_server_host`.
Upload the code to you ESP32 AI Thinker Cam board. Please test the Arduino camera example before you test this code!

2. Install the missing python requirements using pip: `pip install pillow websockets flask asyncio`

3. Run `python receive_stream.py`
You should get a constant stream of numbers (sizes of images). The image.jpg in the directory is always the latest received image.

4. Open a second terminal and run `python send_image_stream.py`
You should get a response by flask with an IP and port to enter in your browser.

Now enjoy your fresh live stream! 📺



# Known Issues
### Browsers don't like broken images.
This is solved using the placeholder.jpg. It just replaces the image, if the backend receives a broken frame to prevent the browser from freezing the stream.

### You have to have the right board.
There are many ESP32 Camera modules. The defined pins in `websocket_camera_stream.ino` only work with the AI Thinker Cam. Change this, if you have a different board. The only tested camera is currently the OV2640.


## Video!
[![LINK TO VIDEO](https://img.youtube.com/vi/cdjgs48OQ6E/0.jpg)](https://www.youtube.com/watch?v=cdjgs48OQ6E)
