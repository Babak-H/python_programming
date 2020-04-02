# PIL library to work with pictures in python :

from PIL import Image

# how to open a image and save it in an Image class object.
img = Image.open("bobby.jpg")

# img.size = width and height of the image in a topple (w, h).
print(img.size)

# img.format = format of the image.
print(img.format)

# show the image in your console
img.show()