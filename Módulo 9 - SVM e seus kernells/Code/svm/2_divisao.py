import cv2

video = cv2.VideoCapture('NamibiaCam.mp4')

n = 20

while True:
    ret, frame = video.read()
    if not ret:
        break

    for i in range(0, frame.shape[1], n):
        for j in range(0, frame.shape[0], n):
            frame = cv2.rectangle(frame, (i, j), (i + n, j + n), (255, 0, 0), 1)

    cv2.imshow('test', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()
