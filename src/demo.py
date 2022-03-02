import cv2
import numpy as np

importPhotoFile = '../photo/demo'
savePhotoFile = '../photo/result'

apple = cv2.imread(importPhotoFile + '/quatao.jfif')
apple = cv2.resize(apple, (400, 400))
orange = cv2.imread(importPhotoFile + '/quacam.jfif')
orange = cv2.resize(orange, (400, 400))
apple_orange = np.hstack((apple[:, :172], orange[:, 200:]))

# generate Gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)


# generate Gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# cv2.imshow("orange", orange)
# cv2.imshow("apple_orange", apple_copy)
# cv2.imshow("apple_orange_reconstruct", apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()