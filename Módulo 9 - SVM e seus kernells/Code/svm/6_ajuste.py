
from PIL import Image
from sklearn import svm
from mss import mss
import numpy as np
import pyautogui
import cv2
from sklearn.model_selection import train_test_split


def normalizeImage(v):
    v = (v - v.min()) / (v.max() - v.min())
    result = (v * 255).astype(np.uint8)
    return result



n = 160

def compute_histogram(img_gray, bins=240):

    hist, _ = np.histogram( 5*(img_gray/250 ), bins=np.arange(bins+1))
    return hist

def generate_histogram_image(hist, width=80, height=80):

    hist_img = np.zeros((height, width), dtype=np.uint8)
    hist_normalized = hist * (height / np.max(hist))
    for i, h in enumerate(hist_normalized.astype(int)):
        cv2.line(hist_img, (i, height), (i, height - h), (255,), 1)
    return hist_img

def mouse_click(event, x, y, flags, param):
    global img_arr, clicked_points

    # Se o botão esquerdo do mouse for clicado
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y, 'left'))

    # Se o botão direito do mouse for clicado
    if event == cv2.EVENT_RBUTTONDOWN:
        clicked_points.append((x, y, 'right'))


clicked_points = []
dataset = []
labels = []
added_points = []
treined = False

clf = svm.SVC(kernel='linear', C=1)

cv2.namedWindow("test")
cv2.setMouseCallback("test", mouse_click)


video = cv2.VideoCapture('NamibiaCam.mp4')


while (True):
    ret, img_arr = video.read()
    if not ret:
        break


    for i in range(0, img_arr.shape[1], n):
        for j in range(0, img_arr.shape[0], n):
            img_arr = cv2.rectangle(img_arr, (i, j), (i+n, j+n), (255, 0, 0), 1)
            if treined:
                # Extract window
                window_img = img_arr[j:j + n, i:i + n, :]

                window_img = cv2.cvtColor(window_img, cv2.COLOR_RGB2BGR )
                hist_features = compute_histogram(cv2.cvtColor(window_img, cv2.COLOR_BGR2GRAY))

                # Predict using SVM
                prediction = clf.predict([hist_features])

                # Color the window based on the prediction
                color = (0, 255, 0) if prediction[0] == 1 else (0, 0, 255)
                cv2.rectangle(img_arr, (i, j), (i + n, j + n), color, 2)


    for x,y, label in clicked_points:
        x_window = x // n
        y_window = y // n

        if (x_window, y_window) not in added_points:
            window_img = img_arr[y_window * n:(y_window + 1) * n, x_window * n:(x_window + 1) * n, :]

            hist_features = compute_histogram(cv2.cvtColor(window_img, cv2.COLOR_BGR2GRAY))


            dataset.append(hist_features)
            labels.append(0 if label == "right" else 1)
            added_points.append((x_window, y_window))


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
        added_points = []
        labels = []
        dataset = []

    if key == ord('t'):
        # Treinar o SVM AQUI
        clf.fit(dataset,labels)
        treined = True
        clicked_points = []
        added_points = []