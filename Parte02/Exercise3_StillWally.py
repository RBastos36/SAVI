
import cv2 as cv
import numpy as np

img1 = cv.imread("Parte02/images/school.jpg")
assert img1 is not None, "file could not be read"

img2 = cv.imread("Parte02/images/beach.jpg")
assert img2 is not None, "file could not be read"

model = cv.imread("Parte02/images/wally.png")
assert model is not None, "file could not be read"

w, h = model.shape[:2]
print(w); print(h)

res1 = cv.matchTemplate(img1, model, cv.TM_CCOEFF_NORMED)
min_val1, max_val1, min_loc1, max_loc1 = cv.minMaxLoc(res1)
print(max_loc1)
center1 = (max_loc1[0] + w // 2, max_loc1[1] + h // 2)

cv.circle(img1, (center1[0], center1[1]), 20, (0, 0, 0), 2)


res2 = cv.matchTemplate(img2, model, cv.TM_CCOEFF_NORMED)
min_val2, max_val2, min_loc2, max_loc2 = cv.minMaxLoc(res2)
print(max_loc2)
center2 = (max_loc2[0] + w // 2, max_loc2[1] + h // 2)

cv.circle(img2, (center2[0], center2[1]), 20, (0, 0, 0), 2)


cv.imshow("Where's Wally?", img1)
cv.imshow("Where's Wally? Again...", img2)
cv.waitKey(0)
cv.destroyAllWindows()