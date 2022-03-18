import PIL
from PIL import Image

width = 600
height = 600

img = Image.open('a.jpg')
img = img.resize((width,height),PIL.Image.ANTIALIAS)
img.save('resize.jpg')