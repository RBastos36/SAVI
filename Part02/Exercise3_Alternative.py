
import cv2 as cv
import numpy as np

point_start = None
point_end = None

def mouseCallback(event, x, y, flags, param):
    global point_start, point_end

    if event == cv.EVENT_LBUTTONDOWN:
        point_start = (x, y)
        print("Point Start Recorded!")
    elif event == cv.EVENT_LBUTTONUP:
        point_end = (x, y)
        print("Point End Recorded!")


while True:
    ans = int(input("Select image to analyse:\n(1) - School\n(2) - Beach\n"))
    if ans == 1:
        scene = cv.imread("Part02/images/school.jpg")
        assert scene is not None, "file could not be read"
        break
    elif ans == 2:
        scene = cv.imread("Part02/images/beach.jpg")
        assert scene is not None, "file could not be read"
        break


cv.imshow('Scene', scene)
cv.setMouseCallback('Scene', mouseCallback)

while True:
    if point_start is not None and point_end is not None:
        break
    cv.waitKey(20)

print("Start Point: {}\nEnd Point: {}".format(point_start, point_end))

template = scene[point_start[1]:point_end[1], point_start[0]:point_end[0]]

cv.imshow("Template", template)
cv.waitKey(1000)

# Find template match in the original image 1, as well as its coordinates
result = cv.matchTemplate(scene, template, cv.TM_CCOEFF_NORMED)
_, max_val, _, max_loc = cv.minMaxLoc(result)

h, w, _ = template.shape

cv.rectangle(scene, (max_loc[0], max_loc[1]), (max_loc[0] + w, max_loc[1] + h), (0,255,0), 3)

# Show the final results
cv.imshow("Where's Wally?", scene)
cv.waitKey(0)
cv.destroyAllWindows()