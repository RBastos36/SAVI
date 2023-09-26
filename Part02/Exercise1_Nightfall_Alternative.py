
import cv2 as cv
import numpy as np


# Open image and verify if path to image exists
img = cv.imread("/home/rantonio/Desktop/SAVI/Parte02/images/lake.jpg")
assert img is not None, "file could not be read, check with os.path.exists()"

rows, cols = img.shape[:2]      # Size of image

# Create black image half the size of the main image
blk_half = np.zeros((rows, cols // 2), np.uint8)
blk_half = cv.cvtColor(blk_half, cv.COLOR_GRAY2BGR)

# Divide the main image in left and right halves
right_half = img[0:rows, cols // 2:cols]
left_half = img[0:rows, 0:cols // 2]

a = 1
b = 1 - a

# Loop to generate frames with the right half darkening over cycles
for i in range(1, 8):
    right_save = cv.addWeighted(right_half, a, blk_half, b, 0)
    img_save = np.hstack((left_half, right_save))
    cv.imwrite("Parte02/Images1/{}.jpg".format(i), img_save)
    cv.imshow("{}".format(i), img_save)
    cv.waitKey(0)
    a -= 0.1
    b = 1 - a


pic_main = np.zeros((585, 780, 3), np.uint8)                # Blank screen for the animation
location = "/home/rantonio/Desktop/SAVI/Parte02/Images1"    # Frames location

img_array = []      # Array to track video frames (images) to save

# Loop to show the frames of the nightfall created above, using a blended animation in between
for file in range(1, 8):  
    pic = cv.imread(location + "/" + str(file) + ".jpg")
    height, width, layers = img.shape
    size = (width, height)

    for alpha in range(1, 11):
        alpha = alpha / 10
        beta = 1 - alpha
        pic_save = cv.addWeighted(pic, alpha, pic_main, beta, 0.0)
        cv.imshow('Nightfall', pic_save)
        cv.waitKey(100)
        img_array.append(pic_save)

    pic_main = pic


# Capturing/Writing os the video frames
out = cv.VideoWriter('Parte02/Nightfall.avi', cv.VideoWriter_fourcc(*'DIVX'), 20, size)

for i in range(len(img_array)):
    out.write(img_array[i])

out.release()       # Ending recording

print("Finished!")
cv.imshow('Nightfall', pic)
cv.waitKey(0)
cv.destroyAllWindows()