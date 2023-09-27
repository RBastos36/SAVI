
import cv2 as cv
import numpy as np


# Read both images
img1 = cv.imread("Part02/images/school.jpg")
assert img1 is not None, "file could not be read"
img2 = cv.imread("Part02/images/beach.jpg")
assert img2 is not None, "file could not be read"

# Select Region of Interest from the first image and convert ROI to Image
model1 = cv.selectROI(img1)
model1_cropped = img1[int(model1[1]):int(model1[1] + model1[3]), int(model1[0]):int(model1[0] + model1[2])]
w, h = model1_cropped.shape[:2]

# Find template match in the original image 1, as well as its coordinates
res1 = cv.matchTemplate(img1, model1_cropped, cv.TM_CCOEFF_NORMED)
min_val1, max_val1, min_loc1, max_loc1 = cv.minMaxLoc(res1)
center1 = (max_loc1[0] + w // 2, max_loc1[1] + h // 2)

# Select Region of Interest from the second image and convert ROI to Image
model2 = cv.selectROI(img2)
model2_cropped = img2[int(model2[1]):int(model2[1] + model2[3]), int(model2[0]):int(model2[0] + model2[2])]
w, h = model2_cropped.shape[:2]

# Find template match in the original image 2, as well as its coordinates
res2 = cv.matchTemplate(img2, model2_cropped, cv.TM_CCOEFF_NORMED)
min_val2, max_val2, min_loc2, max_loc2 = cv.minMaxLoc(res2)
center2 = (max_loc2[0] + w // 2, max_loc2[1] + h // 2)

# Clear any windows openned (because of cv.selectROI())
cv.destroyAllWindows()

# Draw circles centered ont the template matches
cv.circle(img1, (center1[0], center1[1]), 20, (0, 0, 0), 2)
cv.circle(img2, (center2[0], center2[1]), 20, (0, 0, 0), 2)

# Show the final results
cv.imshow("Where's Wally?", img1)
cv.imshow("Where's Wally? Again...", img2)
cv.waitKey(0)
cv.destroyAllWindows()