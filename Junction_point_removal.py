import cv2
import numpy as np
img = cv2.imread("final.png")

def neighbours(x,y,image):

    img = image
    x_1, y_1, x1, y1 = x-1, y-1, x+1, y+1;
    return [ img[x_1][y], img[x_1][y1], img[x][y1], img[x1][y1], img[x1][y], img[x1][y_1], img[x][y_1], img[x_1][y_1] ]

#img = list(img)
#img[0][0]=[0,0,0]
#print(img[0][0])
for x in range(0,len(img)-1):
    for y in range(0,len(img[x])-1):
	#print(img[x][y])
	nbrs=neighbours(x,y,img)
	black_C=0
	#print(type(nbrs))
	i=0
	for n in nbrs:
		#print(n)
		if(n[0]==255 and n[1]==255 and n[2]==255 ):
				
			i+=1	

		if(i>=3):
			print(img[x][y])
			img[x][y]=[0,0,0]
			print(img[x][y])



from PIL import Image
im = Image.fromarray(img)
im.save("done.png")
