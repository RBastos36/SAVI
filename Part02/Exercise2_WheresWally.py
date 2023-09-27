
import cv2 as cv
import numpy as np

# Read the image and the respective template
img = cv.imread("Part02/images/scene.jpg")
assert img is not None, "file could not be read"
model = cv.imread("Parte02/images/wally.png")
assert model is not None, "file could not be read"

# Size of the template
w, h = model.shape[:2]

# Find location of the object within the main image and its coordinates
res = cv.matchTemplate(img, model, cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
center = (max_loc[0] + w // 2, max_loc[1] + h // 2)         # Center of the circle in middle of object

# Draw circle in the middle of the object
cv.circle(img, (center[0], center[1]), 20, (20, 255, 57), 2)

cv.imshow("Where's Wally?", img)
cv.waitKey(0)
cv.destroyAllWindows()