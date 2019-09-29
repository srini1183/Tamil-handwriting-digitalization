import cv2

name = 'img1.png'
im1 = cv2.imread(name)
width = 200
height = 200
im2 = cv2.resize(im1,(width, height))
cv2.imwrite(name,im2)

