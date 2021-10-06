import cv2
from matplotlib import pyplot as plt
import easygui

def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        y1 = y-100 if y-100 >= 0 else 0
        x1 = x-100 if x-100 >= 0 else 0
        y2 = y+100 if y+100 <= I.shape[0] else I.shape[0]
        x2 = x+100 if x+100 <= I.shape[1] else I.shape[1]
        
        cv2.rectangle(img=I,pt1 =(x1,y1),pt2 =(x2,y2),color=(0,0,255),thickness = 5) #draw rectangle
        
        I[y1:y2,x1:x2] = cv2.cvtColor(I[y1:y2,x1:x2], cv2.COLOR_BGR2YUV) #convert area inside square to yuv
        cv2.imshow("image",I)

f = easygui.fileopenbox()
I = cv2.imread(f)

cv2.namedWindow("image")
cv2.setMouseCallback("image",draw)

cv2.imshow("image",I)
cv2.waitKey(0)