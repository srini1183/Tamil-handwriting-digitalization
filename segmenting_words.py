import cv2
import numpy as np

# Load the image
img = cv2.imread('tamil.png')

# convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#cv2.imshow('gray',gray)

# smooth the image to avoid noises
gray = cv2.medianBlur(gray,5)

# Apply adaptive threshold
thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
thresh_color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)

# apply some dilation and erosion to join the gaps
thresh = cv2.dilate(thresh,None,iterations = 3)
thresh = cv2.erode(thresh,None,iterations = 2)




# Find the contours
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
contours = sorted(contours, key=lambda contours : cv2.boundingRect(contours )[0] + cv2.boundingRect(contours)[1] * img.shape[1])

print("Number of Contours found = " + str(len(contours))) 
#print(cnts)
#print(boundingBoxes)
i=0
# For each contour, find the bounding rectangle and draw it
print(type(contours))
for cnt in contours:
    

    x,y,w,h = cv2.boundingRect(cnt)
    print(x,y,w,h)    
    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.rectangle(thresh_color,(x,y),(x+w,y+h),(0,255,0),2)
    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite("output4/"+str(i)+".png",crop_img)
    i=i+1 
    	
   
