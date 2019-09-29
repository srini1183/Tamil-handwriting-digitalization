import cv2
import numpy as np
from PIL import Image

# Load as greyscale
im = cv2.imread('sample_output3/img3.png', cv2.IMREAD_GRAYSCALE)

# Invert
im = 255 - im

# Calculate vertical projection
proj = np.sum(im,0)
print(proj)
proj = list(proj)

h,w =im.shape
print(h,w)

while(proj[w-1]==0):
 proj.pop(w-1)
 w=w-1


start=0
end=0
k=0
prev=0
x=0
while(x<w):
 prev=end
 if(proj[x]!=0):
   start=x
 if(proj[x]==0):
  while(x<w and proj[x]==0):
     x=x+1
  start=x
 if(proj[x]!=0):
   while(x<w and proj[x]!=0):
       x=x+1
   end=x - 1
 if(prev==end):
   end=w-1
 print(start)
 print(end) 
 img = Image.open("sample_output3/img3.png")
 area = (start,0,end,h)
 img = img.crop(area)
 img.save("sample_output3/sample"+str(k)+".png")
 k=k+1




