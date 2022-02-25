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

rectangleWidth1 = 150
rectangleHeight1 = 150

rectangleWidth2 = 190
rectangleHeight2 = 190

rectangleWidth3 = 230
rectangleHeight3 = 230

list_draw = []

center = np.zeros((width, height, 3), np.uint8)

def drawShape(positionX, positionY, degree):
    img = cv.rectangle(center, ((int)(width / 2 - positionX), (int)(height / 2 - positionY)), ((int)(width / 2 + positionX), (int)(height / 2 + positionY)), (0, 255, 0), 3)
    return ndimage.rotate(img, degree)

center = drawShape(rectangleWidth2, rectangleHeight2, 30)
center = drawShape(rectangleWidth3, rectangleHeight3, 45)

# show image
cv.imshow("Display window", center)

while(True):
    k = cv.waitKey(1)
    if k == ord('q'):
        break
  
cv.destroyAllWindows() 
