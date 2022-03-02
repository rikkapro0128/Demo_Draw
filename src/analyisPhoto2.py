import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

rows = 2
cols = 4

importPhotoFile = '../photo/demo'
savePhotoFile = '../photo/result'

imgHandle = cv.imread(importPhotoFile + "/coins.jpg")
gray = cv.cvtColor(imgHandle, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

# Read image
im = cv.imread(importPhotoFile + "/BlobTest.jpg", cv.IMREAD_GRAYSCALE)
# Set up the detector with default parameters.
detector = cv.SimpleBlobDetector_create()
# Detect blobs.
keypoints = detector.detect(im)
# Draw detected blobs as red circles.
# cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv.drawKeypoints(im, keypoints, np.zeros((1,1)), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

kernel = np.ones((3,3),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)
# sure background area
sure_bg = cv.dilate(opening,kernel,iterations=3)
# Finding sure foreground area
dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers + 1
# Now, mark the region of unknown with zero
markers[unknown == 255] = 0

markers = cv.watershed(imgHandle, markers)
imgHandle[markers == -1] = [255, 0, 0]

# def watershedHandle(imgHandle): 
#     imgHandle = cv.imread(imgHandle)
#     gray = cv.cvtColor(imgHandle, cv.COLOR_BGR2GRAY)
#     ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)


def grabCutHandle(imgHandle): 
    img = cv.imread(imgHandle)
    mask = np.zeros(img.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    rect = (50,50,450,290)
    cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]
    return img

def imgConnectTwoImage(img1, img2): 
    apple = cv.imread(img1)
    apple = cv.resize(apple, (400, 400))
    orange = cv.imread(img2)
    orange = cv.resize(orange, (400, 400))
    return np.hstack((apple[:, :172], orange[:, 200:]))

fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(15,15))

for i in range(rows):
    for j in range(cols):        
            axes[i, j].get_xaxis().set_visible(False)
            axes[i, j].get_yaxis().set_visible(False)

axes[0, 0].imshow(thresh)
axes[0, 1].imshow(unknown)
axes[0, 2].imshow(imgHandle)
axes[0, 3].imshow(im_with_keypoints)
axes[1, 0].imshow(grabCutHandle(importPhotoFile + "/gaixinh.jfif"))
axes[1, 1].imshow(imgConnectTwoImage(importPhotoFile + "/quatao.jfif", importPhotoFile + "/quacam.jfif"))

plt.show()
# cv.waitKey(0)