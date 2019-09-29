import glob
import cv2
import numpy as np
import xlwt 
from xlwt import Workbook 

wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1',cell_overwrite_ok=True) 
sheet1.write(0,0,'IMAGE NAME')
sheet1.write(0,1,'PIXEL DENSITY(NO OF BLACK PIXELS/TOTAL NO OF PIXELS)')
path = '/home/guest/slice'
i=1
files = [f for f in glob.glob(path + "**/*.png")]
count = 0
for f in files:
   print(f)
   count = 0
   i=i+1
   img = cv2.imread(f)
   for x in range(0,len(img)-1):
     for y in range(0,len(img[x])-1):
	if(list(img[x][y])==[255,255,255]):
		count+=1
        
	sheet1.write(i,0,f)
        sheet1.write(i,1,count/60.0)
   

wb.save('Pixel_Density.xls') 
