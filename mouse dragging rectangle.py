import cv2
import numpy as np

img = np.zeros((512,512,3))

# IF WE MOVE THE MOUSE, EVENT WILL BE 0
# IF WE CLICK THE MOUSE, EVENT WILL BE 1
# IF WE DE-CLICK THE MOUSE, EVENT WILL BE 4

flag = False
ix = -1
iy = -1

def draw(event,x,y,flags,params):
    global flag, ix, iy
    if event == 1:
        flag = True
        ix = x
        iy = y
    
    elif event == 0:
        if flag == True:
            cv2.rectangle(img, pt1=(ix,iy),pt2=(x,y), color=(0,0,255), thickness=-1)
    
    elif event == 4:
        flag = False
        cv2.rectangle(img, pt1=(ix,iy),pt2=(x,y), color=(0,0,255), thickness=-1)



cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", draw)   #THIS WILL DETECT THE MOUSE EVENTS

while True:
    cv2.imshow("window",img) 
    
    if cv2.waitKey(1) & 0xFF == ord("x"): #THIS MEANS THE IMAGE WILL STAY ON WINDOWS FOR 1 SEC & PRESS x TO CLOSE ALL THE WINDOWS
        break 

cv2.destroyAllWindows()

