# Programe to find Resolution(Size) of a Image

import PIL 
from PIL import Image

img = PIL.Image.open("C:/Users/HP/Pictures/Screenshots/Screenshot (1)")
width, height = img.size

print(width, "X", height)