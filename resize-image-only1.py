__author__ = 'webon'

from pillow import Image
import glob, os

size = 200, 200

for infile in glob.glob('C:/Users/webon/Desktop/loan-officer-images.2902jpg'):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + '.thumbnail', 'JPEG')