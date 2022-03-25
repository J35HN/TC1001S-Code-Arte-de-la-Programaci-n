from random import randint
import time
import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
final_image = cv2.imread(f'./img/{randint(1,11)}.png')


def apply_filter(imagen, fc, x, y, w, h):
    face_width = w
    face_height = h

    img_width = int(face_width*1.5) + 1
    img_height = int(1*face_height) + 1
    imagen = cv2.resize(imagen, (img_width, img_height))

    for i in range(img_height):
        for j in range(img_width):
            for k in range(3):
                if imagen[i][j][k] < 200:
                    fc[y + i - int(1.25 * face_height)][x + j -
                                                        int(0.2 * face_width)][k] = imagen[i][j][k]

    return fc

webcam = cv2.VideoCapture(0)

while True:

    used_image = final_image

    size = 4
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    fl = face.detectMultiScale(gray, 1.19, 7)

    for (x, y, w, h) in fl:
        im = apply_filter(used_image, im, x, y, w, h)

    cv2.imshow('Video Con Filtro', im)
    key = cv2.waitKey(30) & 0xff
    if key == 27:  # The Esc key
        break
