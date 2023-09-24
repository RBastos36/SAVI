
import cv2 as cv
import numpy as np
import os

# Open image and verify if path to image exists
img = cv.imread("/home/rantonio/Desktop/SAVI/Parte02/images/lake.jpg")
assert img is not None, "file could not be read, check with os.path.exists()"

rows, cols = img.shape[:2]      # Size of image

# Modify bgr values of every pixel in the right half of the photo and change it,
# progressively, to a darker color, saving the image at the end of the cycle
for i in range(1, 6):
    for row in range(rows):
        for col in range(cols // 2, cols):
            blue = img[row, col, 0]
            green = img[row, col, 1]
            red = img[row, col, 2]
            img[row, col, 0] = abs(blue - i * 5)
            img[row, col, 1] = abs(green - i * 5)
            img[row, col, 2] = abs(red - i * 5)
    cv.imwrite("Parte02/Images1/{}.jpg".format(i), img)


pic_main = np.zeros((585, 780, 3), np.uint8)                # Blank screen for the animation
location = "/home/rantonio/Desktop/SAVI/Parte02/Images1"    # Frames location

img_array = []      # Array to track video frames (images) to save

# Loop to show the frames of the nightfall created above, using a blended animation in between
for file in range(1, 6):  
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