import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

#D:\\Documents\\baggageAI\\threats_resized\\*.jpg

# ap = argparse.ArgumentParser()
# ap.add_argument("-b", "--bag", required=True,
# 	help="path to background images")
# ap.add_argument("-t", "--thrt", required=True,
# 	help="path to threat images")
# args = vars(ap.parse_args())

bag_img = cv2.imread('background_images/BAGGAGE_20180811_175323_83216_B_1.jpg')
thrt_img = cv2.imread('threats_resized/t0.jpg')

# cv2.imshow("bag", bag_img)
# cv2.imshow("thrt", thrt_img)
# cv2.waitKey(0)

x_offset = 62
y_offset = 80

rows,columns,chanels = thrt_img.shape
roi = bag_img[y_offset:205, x_offset:187]

cv2.imshow("roi", roi)
cv2.waitKey(0)

thrt_img_gray = cv2.cvtColor(thrt_img, cv2.COLOR_RGB2GRAY)
blurred = cv2.GaussianBlur(thrt_img_gray, (7, 7), 0)

cv2.imshow("thrt", blurred)
cv2.waitKey(0)

mask = cv2.adaptiveThreshold(blurred, 255,
	cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 4)
cv2.imshow("Mean Adaptive Thresholding", mask)
cv2.waitKey(0)

bg = cv2.bitwise_or(roi,roi,mask = mask)
cv2.imshow("bg", bg)
cv2.waitKey(0)

mask_inv = cv2.bitwise_not(blurred)
cv2.imshow("mask_inv", mask_inv)
cv2.waitKey(0)

fg = cv2.bitwise_and(thrt_img, thrt_img, mask = mask_inv)
cv2.imshow("fg",fg)
cv2.waitKey(0)

final_roi = cv2.add(bg,fg)
cv2.imshow("fr", final_roi)
cv2.waitKey(0)

thrt_img = final_roi

bag_img[y_offset : y_offset + thrt_img.shape[0], x_offset : x_offset + thrt_img.shape[1]] = thrt_img
cv2.imshow("bag-image",bag_img)
cv2.waitKey(0)
