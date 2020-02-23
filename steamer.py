from flask_opencv_streamer.streamer import Streamer
import cv2

port = 3030
require_login = False
streamer = Streamer(port, require_login)

# Open video device 0
video_capture = cv2.VideoCapture(0)

while True:
    _, frame = video_capture.read()

    streamer.update_frame(frame)

    if not streamer.is_streaming:
        streamer.start_streaming()

    cv2.waitKey(30)
