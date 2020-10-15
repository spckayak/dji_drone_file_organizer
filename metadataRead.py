#!/usr/bin/env python

from PIL import Image

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

exif = get_exif('image.jpg')
print(exif)