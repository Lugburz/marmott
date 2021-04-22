import glob, os, sys
from PIL import Image

size = 300, 350

os.chdir("./img/comics")
for file in glob.glob("*.jpg"):
    outfile =  "./thumbnails/" + os.path.basename(file)
    print(outfile)
    if outfile != file:
        try:
            im = Image.open(file)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for '%s'" % file)