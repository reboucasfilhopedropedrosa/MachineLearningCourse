import random
import threading
import time
import joblib
from skimage.feature import local_binary_pattern
from statistics import median
from PIL import ImageGrab
import win32api, win32con
import numpy as np
import cv2
from sklearn import svm

import featureExtractors
from featureExtractors import LBP_FE




n = 80


def mouse_click(event, x, y, flags, param):
    global img_arr, clicked_points

    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y, 'left'))
    if event == cv2.EVENT_RBUTTONDOWN:
        clicked_points.append((x, y, 'right'))



video = cv2.VideoCapture('NamibiaCam.mp4')



clicked_points = []

cv2.namedWindow("test")
cv2.setMouseCallback("test", mouse_click)


while (True):

    ret, img_arr = video.read()
    if not ret:
        break


    for i in range(0, img_arr.shape[1], n):
        for j in range(0, img_arr.shape[0], n):
            img_arr = cv2.rectangle(img_arr, (i, j), (i+n, j+n), (255, 0, 0), 1)

    for x,y, label in clicked_points:
        x_window = x // n
        y_window = y // n

        if label == "right":
            img_arr[y_window * n:(y_window + 1) * n, x_window * n:(x_window + 1) * n, :] = \
            ((img_arr[y_window * n:(y_window + 1) * n,
              x_window * n:(x_window + 1) * n,:] + [0, 0, 255]) // 2).astype(np.uint8)
        else:
            img_arr[y_window * n:(y_window + 1) * n, x_window * n:(x_window + 1) * n, :] = \
                ((img_arr[y_window * n:(y_window + 1) * n,
                  x_window * n:(x_window + 1) * n, :] + [0, 255, 0]) // 2).astype(np.uint8)

    cv2.imshow("test", img_arr)
    key = cv2.waitKey(1)

    # se a tecla 'h' for pressionada, limpe os clicked_points
    if key == ord('h'):
        clicked_points = []