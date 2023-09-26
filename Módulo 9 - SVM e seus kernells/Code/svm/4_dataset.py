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


def normalizeImage(v):
    v = (v - v.min()) / (v.max() - v.min())
    result = (v * 255).astype(np.uint8)
    return result

n = 80

def compute_histogram(img_gray, bins=80):

    hist, _ = np.histogram(img_gray, bins=np.arange(bins+1))
    return hist

def generate_histogram_image(hist, width=80, height=80):

    hist_img = np.zeros((height, width), dtype=np.uint8)
    hist_normalized = hist * (height / np.max(hist))
    for i, h in enumerate(hist_normalized.astype(int)):
        cv2.line(hist_img, (i, height), (i, height - h), (255,), 1)
    return hist_img

def mouse_click(event, x, y, flags, param):
    global img_arr, clicked_points
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y, 'left'))

    if event == cv2.EVENT_RBUTTONDOWN:
        clicked_points.append((x, y, 'right'))


clicked_points = []
dataset = []
labels = []
added_points = []

video = cv2.VideoCapture('NamibiaCam.mp4')


cv2.namedWindow("test")
cv2.setMouseCallback("test", mouse_click)

cv2.namedWindow("Histogram")
cv2.moveWindow("Histogram", 1280, 0)

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

        if (x_window, y_window) not in added_points:
            window_img = img_arr[y_window * n:(y_window + 1) * n, x_window * n:(x_window + 1) * n, :]

            hist_features = compute_histogram(cv2.cvtColor(window_img, cv2.COLOR_BGR2GRAY))
            hist_img = generate_histogram_image(hist_features)

            img_arr[y_window * n:(y_window + 1) * n, x_window * n:(x_window + 1) * n, 0] = hist_img
            img_arr[y_window * n:(y_window + 1) * n, x_window * n:(x_window + 1) * n, 1] = hist_img
            img_arr[y_window * n:(y_window + 1) * n, x_window * n:(x_window + 1) * n, 2] = hist_img

            dataset.append(hist_features)
            labels.append(0 if label == "right" else 1)
            added_points.append((x_window, y_window))

            cv2.imshow("Histogram", normalizeImage(hist_img))

            key = cv2.waitKey(1)


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

    if key == ord('h'):
        print(dataset)
        print(labels)
        clicked_points = []
        added_points = []
        labels = []