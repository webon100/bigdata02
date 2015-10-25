__author__ = 'webon'

#import os
#import getopt
#import sys
from PIL import Image


# Open the image file.
imageFile = "C:/Users/webon/Desktop/loan-officer-images/2902.jpg"
img = Image.open(imageFile)

BaseWidth = 200

# Calculate the height using the same aspect ratio
widthPercent = (BaseWidth / float(img.size[0]))
height = int((float(img.size[1]) * float(widthPercent)))

# Resize it.
#img = img.resize((BaseWidth, height), Image.BILINEAR)
img = img.resize((BaseWidth, height), Image.ANTIALIAS)
ext = ".jpg"

img.save("C:/Users/webon/Desktop/loan-officer-images/ANTIALIAS-2902-fix200" + ext)



# Iterate through every image given in the directory argument and resize it.
for image in os.listdir(directory):
    print('Resizing image ' + image)

    # Open the image file.
    img = Image.open(os.path.join('C:/Users/webon/Desktop/loan-officer-images', image))

    # Resize it.
    img = img.resize((width='400', height='450'), Image.BILINEAR)

    # Save it back to disk.
    img.save(os.path.join('C:/Users/webon/Desktop/loan-officer-images', 'resized-400-450' + image))

print('Batch processing complete.')




