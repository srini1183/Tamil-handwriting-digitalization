from PIL import Image

img = Image.open("018.jpeg")
area = (59,31,6,12)
img = img.crop(area)
img.save("sam.jpeg")


