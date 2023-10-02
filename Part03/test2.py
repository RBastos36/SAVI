import cv2
from time import sleep


delay = 60
detect = []
cars = 0
offset = 10

line_height = 350


def get_center(x, y, w, h):

    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


bg_subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 31))
# morph_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

cap = cv2.VideoCapture('Part03/docs/traffic.mp4')
success, frame = cap.read()

while success:

    # stime = float(1/delay)         
    # sleep(stime)

    fg_mask = bg_subtractor.apply(frame)
    _, thresh = cv2.threshold(fg_mask, 244, 255, cv2.THRESH_BINARY)
    cv2.erode(thresh, erode_kernel, thresh, iterations=3)
    cv2.dilate(thresh, dilate_kernel, thresh, iterations=3)
    # cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, morph_kernel, thresh)

    contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame, (15, line_height), (1250, line_height), (0, 0, 0), 2)

    for c in contours:
        if cv2.contourArea(c) > 1000:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
            center = get_center(x, y, w, h)                    
            detect.append(center)
            cv2.circle(frame, center, 4, (0, 0, 255), -1)

        for (x, y) in detect:                 
            
            if (y < (line_height + offset)) and (y > (line_height - offset)):
                cars += 1
                cv2.line(frame, (25, line_height), (1200, line_height), (255, 0, 255), 3)
                detect.remove((x, y))
                print("No. of cars detected : " + str(cars))
                
    
    
    cv2.putText(frame, "VEHICLE COUNT: "+str(cars), (50, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 4)

    cv2.imshow('mog', fg_mask)
    cv2.imshow('thresh', thresh)
    cv2.imshow('detection', frame)


    k = cv2.waitKey(30)

    if k == 27: # Escape
        break

    success, frame = cap.read()

cv2.destroyAllWindows()
cap.release()