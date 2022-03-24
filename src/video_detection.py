
import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
riddler=cv2.imread('./img/Gordon.png')



def apply_filter(glasses2022, fc, x, y, w, h):
    face_width = w
    face_height = h

    hat_width = int(face_width*1.5) + 1
    hat_height = int(1*face_height) + 1
    glasses2022 = cv2.resize(glasses2022, (hat_width, hat_height))

    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if glasses2022[i][j][k] < 200:
                    fc[y + i -int(1.25 * face_height)][x + j-int(0.2 * face_width)][k] = glasses2022[i][j][k]

    return fc

global choise

choice = 0
print('enter your choice filter to launch that: 1="put hat & glasses" ,any number="put fog filters" ')
choise= int(input('enter your choice:'))
webcam = cv2.VideoCapture(0)


while True:
    size=4
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    fl = face.detectMultiScale(gray,1.19,7)

    for (x, y, w, h) in fl:
        im=apply_filter(riddler, im, x,y,w,h)


    cv2.imshow('Video Con Filtro',im)
    key = cv2.waitKey(30) & 0xff
    if key == 27:  # The Esc key
       break