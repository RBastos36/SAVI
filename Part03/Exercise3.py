import cv2
import numpy as np


delay = 60
detect = []
check_x = None
check_y = None
cars = 0
offset = 10
lane1 = 0
lane2 = 0
lane3 = 0
lane4 = 0

red_lower = np.array([136, 87, 111], np.uint8)
red_upper = np.array([180, 255, 255], np.uint8)
green_lower = np.array([25, 52, 72], np.uint8)
green_upper = np.array([102, 255, 255], np.uint8)
blue_lower = np.array([94, 80, 2], np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)
yellow_lower = np.array([25,100,100])
yellow_upper = np.array([30,255,255])
dark_teal_lower = np.array([0,0,200])
dark_teal_upper = np.array([180,255,255])
bright_teal_lower = np.array([0,0,0])
bright_teal_upper = np.array([180,255,100])

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

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

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



                color = hsvFrame[center[1], center[0]]
                if red_lower[0] <= color[0] <= red_upper[0] and red_lower[1] <= color[1] <= red_upper[1] and red_lower[2] <= color[2] <= red_upper[2]:
                    color_str =  'Red'
                elif green_lower[0] <= color[0] <= green_upper[0] and green_lower[1] <= color[1] <= green_upper[1] and green_lower[2] <= color[2] <= green_upper[2]:
                    color_str = 'Green'
                elif blue_lower[0] <= color[0] <= blue_upper[0] and blue_lower[1] <= color[1] <= blue_upper[1] and blue_lower[2] <= color[2] <= blue_upper[2]:
                    color_str = 'Blue'
                elif yellow_lower[0] <= color[0] <= yellow_upper[0] and yellow_lower[1] <= color[1] <= yellow_upper[1] and yellow_lower[2] <= color[2] <= yellow_upper[2]:
                    color_str = 'Yellow'
                elif dark_teal_lower[0] <= color[0] <= dark_teal_upper[0] and dark_teal_lower[1] <= color[1] <= dark_teal_upper[1] and dark_teal_lower[2] <= color[2] <= dark_teal_upper[2]:
                    color_str = 'Dark Color'
                elif bright_teal_lower[0] <= color[0] <= bright_teal_upper[0] and bright_teal_lower[1] <= color[1]<= bright_teal_upper[1] and bright_teal_lower[2] <= color[2] <= bright_teal_upper[2]:
                    color_str = 'Bright Color'
                else:
                    color_str = 'Other'


                lane = 0
                if (200 <= x <= 495):
                   lane1 += 1
                   lane = 1
                   print("No. of cars detected: {}\nTotal by Lane: [{}] [{}] [{}] [{}]\n".format(str(cars),
                                                                                                 str(lane1), str(lane2), str(lane3), str(lane4)))
                   cv2.line(frame, (200, line_height), (495, line_height), (255, 0, 255), 3)
                   
                elif (495 < x <= 660):
                   lane2 += 1
                   lane = 2
                   print("No. of cars detected: {}\nTotal by Lane: [{}] [{}] [{}] [{}]\n".format(str(cars),
                                                                                                 str(lane1), str(lane2), str(lane3), str(lane4)))
                   cv2.line(frame, (495, line_height), (660, line_height), (255, 0, 255), 3)

                elif(660 < x <= 840):
                   lane3 += 1
                   lane = 3
                   print("No. of cars detected: {}\nTotal by lane: [{}] [{}] [{}] [{}]\n".format(str(cars),
                                                                                                 str(lane1), str(lane2), str(lane3), str(lane4)))
                   cv2.line(frame, (660, line_height), (840, line_height), (255, 0, 255), 3)

                elif (840 < x <= 1200):
                   lane4 += 1
                   lane = 4
                   print("No. of cars detected: {}\nTotal por Faixa: [{}] [{}] [{}] [{}]\n".format(str(cars),
                                                                                                 str(lane1), str(lane2), str(lane3), str(lane4)))
                   cv2.line(frame, (840, line_height), (1200, line_height), (255, 0, 255), 3)
                
                print("Last car in lane no. {}; Color: {}\n".format(str(lane), color_str))
                
    
    
    cv2.putText(frame, "VEHICLE COUNT: "+str(cars), (50, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 4)
    cv2.putText(frame, "[{}] [{}] [{}] [{}]".format(str(lane1), str(lane2), str(lane3), str(lane4)), (50, 140), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 4)

    cv2.imshow('mog', fg_mask)
    cv2.imshow('thresh', thresh)
    cv2.imshow('detection', frame)


    k = cv2.waitKey(30)

    if k == 27: # Escape
        break

    success, frame = cap.read()

cv2.destroyAllWindows()
cap.release()