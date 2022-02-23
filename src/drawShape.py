import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy import ndimage
from PIL import Image
import matplotlib
import pathlib

importPhotoFile = '../photo/demo'
savePhotoFile = '../photo/result'

width = 500
height = 500

rectangleWidth = 150
rectangleHeight = 150

rectangleWidth2 = 190
rectangleHeight2 = 190

list_draw = []

img = np.zeros((width, height, 3), np.uint8)
img = cv.rectangle(img, ((int)(width / 2 - rectangleWidth), (int)(height / 2 - rectangleHeight)), ((int)(width / 2 + rectangleWidth), (int)(height / 2 + rectangleHeight)), (0, 255, 0), 3)
# image_center = tuple(np.array(img.shape[1::-1]) / 2)
img = ndimage.rotate(img, 45)

img = cv.rectangle(img, ((int)(width / 2 - rectangleWidth), (int)(height / 2 - rectangleHeight)), ((int)(width / 2 + rectangleWidth), (int)(height / 2 + rectangleHeight)), (0, 255, 0), 3)

# if file not found
if img is None:
    sys.exit("Could not read the image.")

# show image
cv.imshow("Display window", img)

while(True):
    k = cv.waitKey(1)
    if k == ord('q'):
        break
  
cv.destroyAllWindows() 
