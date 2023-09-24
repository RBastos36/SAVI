
import cv2 as cv


img = cv.imread("/home/rantonio/Desktop/SAVI/Parte02/images/lake.jpg")
assert img is not None, "file could not be read, check with os.path.exists()"

cv.imshow("Picture", img)
cv.waitKey(0)
cv.destroyAllWindows()