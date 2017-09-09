import numpy as np
import cv2
import glob

# Define the chess board rows and columns
rows = 7
cols = 6

# Set the termination criteria for the corner sub-pixel algorithm
criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 30, 0.001)

# Prepare the object points: (0,0,0), (1,0,0), (2,0,0), ..., (6,5,0). They are the same for all images
objectPoints = np.zeros((rows * cols, 3), np.float32)
objectPoints[:, :2] = np.mgrid[0:rows, 0:cols].T.reshape(-1, 2)

# Create the arrays to store the object points and the image points
objectPointsArray = []
imgPointsArray = []

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (rows, cols), None)
    if ret:
    	corners=cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

    	objectPointsArray.append(objectPoints)
    	imgPointsArray.append(corners)

    	cv2.drawChessboardCorners(img, (rows, cols), corners, ret)
    	
 
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
