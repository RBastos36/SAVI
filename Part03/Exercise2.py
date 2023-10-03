import cv2


delay = 60
detect = []
check_x = None
check_y = None
cars = 0
offset = 10
faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0

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

cap = cv2.VideoCapture('Part03/docs/traffic.mp4')
success, frame = cap.read()

while success:


    fg_mask = bg_subtractor.apply(frame)
    _, thresh = cv2.threshold(fg_mask, 244, 255, cv2.THRESH_BINARY)
    cv2.erode(thresh, erode_kernel, thresh, iterations=3)
    cv2.dilate(thresh, dilate_kernel, thresh, iterations=3)

    contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame, (200, line_height), (495, line_height), (0, 0, 0), 2)
    cv2.line(frame, (495, line_height), (660, line_height), (0, 0, 0), 2)
    cv2.line(frame, (660, line_height), (840, line_height), (0, 0, 0), 2)
    cv2.line(frame, (840, line_height), (1200, line_height), (0, 0, 0), 2)

    for c in contours:
        if cv2.contourArea(c) > 1000:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
            center = get_center(x, y, w, h)
            if check_x is None and check_y is None:
                detect.append(center)
            else:
              if check_x - offset <= center[0] <= check_x + offset and check_y - offset <= center[1] <= check_y + offset:
                pass
              else:
                detect.append(center)
                check = []
            cv2.circle(frame, center, 4, (0, 0, 255), -1)

        for (x, y) in detect:
            
            if (y < (line_height + offset)) and (y > (line_height - offset)):
                cars += 1
                detect.remove((x, y))
                check_x = x
                check_y = y
                # print("No. of cars detected: " + str(cars))

                if (200 <= x <= 495):
                   faixa1 += 1
                   print("No. of cars detected: {}\nTotal por Faixa: [{}] [{}] [{}] [{}]\n".format(str(cars),
                                                                                                 str(faixa1), str(faixa2), str(faixa3), str(faixa4)))
                   cv2.line(frame, (200, line_height), (495, line_height), (255, 0, 255), 3)
                   
                elif (495 < x <= 660):
                   faixa2 += 1
                   print("No. of cars detected: {}\nTotal por Faixa: [{}] [{}] [{}] [{}]\n".format(str(cars),
                                                                                                 str(faixa1), str(faixa2), str(faixa3), str(faixa4)))
                   cv2.line(frame, (495, line_height), (660, line_height), (255, 0, 255), 3)

                elif(660 < x <= 840):
                   faixa3 += 1
                   print("No. of cars detected: {}\nTotal by lane: [{}] [{}] [{}] [{}]\n".format(str(cars),
                                                                                                 str(faixa1), str(faixa2), str(faixa3), str(faixa4)))
                   cv2.line(frame, (660, line_height), (840, line_height), (255, 0, 255), 3)

                elif (840 < x <= 1200):
                   faixa4 += 1
                   print("No. of cars detected: {}\nTotal por Faixa: [{}] [{}] [{}] [{}]\n".format(str(cars),
                                                                                                 str(faixa1), str(faixa2), str(faixa3), str(faixa4)))
                   cv2.line(frame, (840, line_height), (1200, line_height), (255, 0, 255), 3)
                
    
    
    cv2.putText(frame, "VEHICLE COUNT: "+str(cars), (50, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 4)
    cv2.putText(frame, "[{}] [{}] [{}] [{}]".format(str(faixa1), str(faixa2), str(faixa3), str(faixa4)), (50, 140), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 4)

    cv2.imshow('mog', fg_mask)
    cv2.imshow('thresh', thresh)
    cv2.imshow('detection', frame)


    k = cv2.waitKey(30)

    if k == 27: # Escape
        break

    success, frame = cap.read()

cv2.destroyAllWindows()
cap.release()