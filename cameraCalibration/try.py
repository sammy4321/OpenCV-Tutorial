'''
 Based on the following tutorial:
   http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_calib3d/py_depthmap/py_depthmap.html
'''

import numpy as np
import cv2

# Load the left and right images in gray scale
imgLeft = cv2.imread('../data/tsukuba_l.png', 0)
imgRight = cv2.imread('../data/tsukuba_r.png', 0)

imgroil = imgLeft[100:200,100:200]
imgroir = imgRight[100:200,100:200]

# Initialize the stereo block matching object 


# Display the result
res = cv2.matchTemplate(imgRight,imgroil,cv2.TM_CCOEFF_NORMED)
w, h = imgroil.shape[::-1]
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
	print(pt[0],pt[1]);cv2.rectangle(imgRight, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)


#cv2.imshow('disparity', np.hstack((imgroil,imgroir)))
cv2.imshow('Image',imgRight)
cv2.imshow('Img',imgroil)
cv2.waitKey(0)
cv2.destroyAllWindows()
