import glob, os, sys
import os.path
from os import path
from PIL import Image

size = 300, 350

os.chdir("./public/img/comics")
for file in glob.glob("*.jpg"):
    outfile =  "./thumbnails/" + os.path.basename(file)
    if not path.exists(outfile):
        try:
            im = Image.open(file)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
            print(outfile)
        except IOError:
            print("cannot create thumbnail for '%s'" % file)