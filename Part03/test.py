
import cv2
import numpy as np
from time import sleep


width_min = 100
height_min = 100
offset = 6
pos_line = 550

# FPS to video
delay = 60

detec = []
cars = 0


def get_center(x, y, w, h):

    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

# Video source input
cap = cv2.VideoCapture('Part03/docs/traffic.mp4')
subtraction = cv2.bgsegm.createBackgroundSubtractorMOG()

success, frame1 = cap.read()  

erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))

while success:

    success, frame1 = cap.read()        
    time = float(1 / delay)         
    sleep(time)

    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = subtraction.apply(blur)
    dilate = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    dilation = cv2.morphologyEx(dilate, cv2. MORPH_CLOSE, kernel)          
    dilation = cv2.morphologyEx(dilation, cv2. MORPH_CLOSE, kernel)          
    contour, h = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)          

    cv2.line(frame1, (25, pos_line), (1200, pos_line), (176, 130, 39), 2)            

    for(i, c) in enumerate(contour):            

        (x, y, w, h) = cv2.boundingRect(c)                
        validate = (w >= width_min) and (h >= height_min)                 

        if not validate:                 
            continue                      

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)                    
        center = get_center(x, y, w, h)                    
        detec.append(center)                     
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)                    

        for (x, y) in detec:                 

            if (y < (pos_line + offset)) and (y > (pos_line - offset)):                         
                cars += 1                          
                cv2.line(frame1, (25, pos_line), (1200, pos_line), (0, 127, 255), 3)                         
                detec.remove((x, y))                        
                print("No. of cars detected : " + str(cars))                        

    cv2.putText(frame1, "VEHICLE COUNT : "+str(cars), (320, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.imshow("Original Video", frame1)
    cv2.imshow(" Detecting ", dilation)

    if cv2.waitKey(1) == 27:
        break        


cv2.destroyAllWindows()
cap.release()