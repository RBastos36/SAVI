
import cv2 as cv
import numpy as np

# Read the image and the respective template
img = cv.imread("Parte02/images/scene.jpg")
assert img is not None, "file could not be read"
model = cv.imread("Parte02/images/wally.png")
assert model is not None, "file could not be read"

# Size of the template
w, h = model.shape[:2]
print(w)
print(h)

# Find location of the object within the main image and its coordinates
res = cv.matchTemplate(img, model, cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + h, top_left[1] + w)

# Convert main image in grayscale and back to BGR to achieve black and white look
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_gray = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)

# Paste Wally in full BGR color
img_gray[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = model

# Show final result
cv.imshow("Test", res)
cv.imshow("Where's Wally?", img_gray)
cv.waitKey(0)
cv.destroyAllWindows()