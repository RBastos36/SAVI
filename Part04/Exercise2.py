
import cv2
import os


with open('Part04/docs/OxfordTownCentre/TownCentre-groundtruth.top', 'r') as f:
    l = [[float(num) for num in line.split(',')] for line in f]

video = cv2.VideoCapture("Part04/docs/OxfordTownCentre/TownCentreXVID.mp4")
ret, frame = video.read()
frame_height, frame_width = frame.shape[:2]
frame = cv2.resize(frame, (frame_width//2, frame_height//2))

if not ret:
    print('Cannot read the video')


while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (frame_width//2, frame_height//2))

    if not ret:
        print('Something went wrong')
        break

    
    cv2.imshow("Tracking", frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
        
video.release()
cv2.destroyAllWindows()
