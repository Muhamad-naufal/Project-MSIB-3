from re import S
import cv2
import numpy as np
import cvzone
from time import sleep
from cvzone.HandTrackingModule import HandDetector 

cap =cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=1)
tombol = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
          ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
          ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]
finaltext = ""

def drawAll(img, buttonlist):

    for button in buttonlist:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h ), (0, 0 ,0), cv2.FILLED)
        cv2.putText(img, button.text, (x + 15, y + 30),
            cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 5)
    return img

class Button():
    def __init__(self, pos, text, size=[50, 50]):
        self.pos = pos
        self.size = size
        self.text = text
        
buttonlist = []
for i in range(len(tombol)):
        for j, tomb in enumerate(tombol[i]):
            buttonlist.append(Button([62 * j + 15, 62 * i + 15], tomb))

while True :
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    img = drawAll(img, buttonlist)

    if lmList:
        for button in buttonlist:
            x,y = button.pos
            w, h = button.size

            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                cv2.rectangle(img, button.pos, (x + w, y + h ), (255, 255, 0), cv2.FILLED)
                cv2.putText(img, button.text, (x + 15, y + 30),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 5) 

                l,_,_ = detector.findDistance(8, 12, img, draw=False)
                print(l)

                # saat di klik
                if l < 30:
                    cv2.rectangle(img, button.pos, (x + w, y + h ), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 15, y + 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 5) 

                    finaltext += button.text
                    sleep(0.15)

        cv2.rectangle(img, (15, 400), (610, 450), (255, 255, 0), cv2.FILLED)
        cv2.putText(img, finaltext, (15, 435),
        cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 6) 

    cv2.imshow("Image", img)
    cv2.waitKey(1)

