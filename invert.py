import cv2
img = cv2.imread("final.png")
img = cv2.bitwise_not(img)
cv2.imwrite('final.png',img)
