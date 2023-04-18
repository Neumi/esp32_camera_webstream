# esp32_camera_webstream
Bringing the ESP32 camera video stream to the web!


The Arduino ESP32-Camera test sketch only lets you use the stream on your local network. To get the stream to the web, you need a bit more...

This collection of scripts consists of:
 - ESP32 code for Arduino
 - python code to receive the images via websockets
 - python code to push the most recent image to a website


 # Why is this cool?
I havent found a working repository that streams ESP32 camera images in real time to a web backend. This sovles this issue.

# How to run?
