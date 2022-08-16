#!/bin/python3
# compressor for JPG files, enabling antialising
# GUI file picker

import PIL
from PIL import Image
from tkinter.filedialog import *
import sys

# ask which file to open
filePath = askopenfilename()

# array of accepted file extensions
acceptedFiles = [".jpg", ".JPG", ".jpeg", ".JPEG"]

# check to make sure the image file is a .JPG image
_count = 0
for i in acceptedFiles:
    if filePath.endswith(i):
        _IMG = PIL.Image.open(filePath)
        _h, _w = _IMG.size
        _IMG = _IMG.resize((_h, _w), PIL.Image.ANTIALIAS)

        savePath = asksaveasfilename()

        _IMG.save(savePath+"_compressed.jpg")
    else:
        _count += 1
        continue

# if file is invalid extension, exit the program and print error message
if _count >= 4:
    print("Sorry, file type is not supported. Only JPG files are supported.")
    sys.exit()