import numpy as np
import cv2

video_capture = cv2.VideoCapture(0)
video_capture.set(3, 160)
video_capture.set(4, 120)

while(True):
    # Capture the frames
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 0)
    frame = cv2.flip(frame, 1)
    # Crop the image
    crop_img = frame[60:120, 0:160]
    # Convert to grayscale
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    # Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Color thresholding
    ret, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)
    # Find the contours of the frame
    contours, hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
    # Find the biggest contour (if detected)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.line(crop_img, (cx, 0), (cx, 720), (255, 0, 0), 1)
        cv2.line(crop_img, (0, cy), (1280, cy), (255, 0, 0), 1)
        cv2.drawContours(crop_img, contours, -1, (0, 255, 0), 1)

        if 60 <= cx <= 120:

            print(0)

        if 168 <= cx <= 180:

            print(1)

        if 156 <= cx < 168:

            print(2)

        if 144 <= cx < 156:

            print(3)

        if 132 <= cx < 144:

            print(4)

        if 120 < cx < 132:

            print(5)

        if 48 <= cx < 60:

            print(6)

        if 36 <= cx < 48:

            print(7)

        if 24 <= cx < 36:

            print(8)

        if 12 <= cx < 24:

            print(9)

        if 0 <= cx < 12:

            print(10)

        else:

            print(11)

    #Display the resulting frame
    cv2.imshow('frame', crop_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break
