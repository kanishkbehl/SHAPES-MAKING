import cv2
import numpy as np

img = np.zeros((512,512,3))

# IF WE MOVE THE MOUSE, EVENT WILL BE 0
# IF WE CLICK THE MOUSE, EVENT WILL BE 1
# IF WE DE-CLICK THE MOUSE, EVENT WILL BE 4


def draw(event,x,y,flags,params):
    if event == 1:
        cv2.circle(img,center=(x,y), radius=50, color=(255,0,0), thickness=-1)


cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", draw)   #THIS WILL DETECT THE MOUSE EVENTS

while True:
    cv2.imshow("window",img) 
    
    if cv2.waitKey(1) & 0xFF == ord("x"): #THIS MEANS THE IMAGE WILL STAY ON WINDOWS FOR 1 SEC & PRESS x TO CLOSE ALL THE WINDOWS
        break 

cv2.destroyAllWindows()

