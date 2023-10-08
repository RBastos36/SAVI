
import cv2
import numpy as np


with open('Part04/docs/OxfordTownCentre/TownCentre-groundtruth.top', 'r') as f:
    l = [[float(num) for num in line.split(',')] for line in f]

l = [[int(num) for num in line] for line in l]

video = cv2.VideoCapture("Part04/docs/OxfordTownCentre/TownCentreXVID.mp4")
ret, frame = video.read()
frame_height, frame_width = frame.shape[:2]
frame = cv2.resize(frame, (frame_width // 2, frame_height // 2))

if not ret:
    print('Cannot read the video')

frameNumber = 0

for line in l:
    if frameNumber == line[1]:
        ret, frame = video.read()
        frame = cv2.resize(frame, (frame_width // 2, frame_height // 2))
        frameNumber += 1

        if not ret:
            print('Something went wrong')
            break
            
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    left = line[8] // 2
    top = line[9] // 2
    right = line[10] // 2
    bottom = line[11] // 2
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    #---------------------------------------------------------
    
    cv2.imshow("Tracking", frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

        
video.release()
cv2.destroyAllWindows()
