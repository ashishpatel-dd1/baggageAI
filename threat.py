import argparse
import cv2
import numpy as np
#import imutils
import glob
import os
from PIL import Image

#D:\\Documents\\baggageAI\\threat_images\\*.jpg

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 0.57)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH), borderValue = (255, 255, 255))

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True,
	help="path to threat images")
args = vars(ap.parse_args())

path = (args["path"])
os.mkdir('threats_resized')
i = 0

for image in glob.glob(path):

    print(image)
    img = cv2.imread(image)


    #Convert to gray, and threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    #Morph-op to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

    #Find the max-area contour
    cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cnt = sorted(cnts, key=cv2.contourArea)[-1]

    #Crop and save it
    x,y,w,h = cv2.boundingRect(cnt)
    dst = img[y:y+h, x:x+w]
    print(dst.shape)

    rotated = rotate_bound(dst, 45)
    
    cv2.imwrite("threats_resized\\t%001i.jpg" %i, rotated)
    i += 1
    cv2.imshow("crop", rotated)
cv2.destroyAllWindows()