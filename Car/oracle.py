#!/usr/bin/python3
import time
import numpy as np
import cv2
from multiprocessing import Process, Queue, Pipe

video_capture = cv2.VideoCapture(0)
video_capture.set(3, 160)
video_capture.set(4, 120)

def oracling(child_conn):
    while (True):

        # Capture the frames
        ret, frame = video_capture.read()
        frame = cv2.flip(frame, 0)
        frame = cv2.flip(frame, 1)
        # Crop the image
        crop_img = frame[90:120, 30:120]
        # Convert to grayscale
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        # Gaussian blur
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # Color thresholding
        ret, thresh = cv2.threshold(blur, 127, 200, cv2.THRESH_BINARY)
        # Find the contours of the frame
        _, contours, hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
        # Find the biggest contour (if detected)
        if (len(contours) > 0):
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            try:

                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

            except:

                val = 13

            cv2.line(crop_img, (cx, 0), (cx, 720), (255, 0, 0), 1)
            cv2.line(crop_img, (0, cy), (1280, cy), (255, 0, 0), 1)
            cv2.drawContours(crop_img, contours, -1, (0, 255, 0), 1)

            if 30 <= cx <= 60:
                val = 0
                child_conn.send(val)

            if 60 < cx <= 66:
                val = 6
                child_conn.send(val)

            if 66 < cx <= 72:
                val = 7
                child_conn.send(val)

            if 72 < cx <= 78:
                val = 8
                child_conn.send(val)

            if 78 < cx <= 84:
                val = 9
                child_conn.send(val)

            if 84 < cx <= 90:
                val = 10
                child_conn.send(val)

            if 24 <= cx < 30:
                val = 1
                child_conn.send(val)

            if 18 <= cx < 24:
                val = 2
                child_conn.send(val)

            if 12 <= cx < 18:
                val = 3
                child_conn.send(val)

            if 6 <= cx < 12:
                val = 4
                child_conn.send(val)

            if 0 <= cx < 6:
                val = 5
                child_conn.send(val)

        else:
            val = 11
            child_conn.send(val)
            time.sleep(5)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            val = 13
            child_conn.send(val)
            child_conn.close()
            break

        cv2.imshow('frame', crop_img)
