import numpy as np 
import cv2

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)
  
#cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
img = cv2.imread('A2.jpg')

if img.shape[0]>img.shape[1] or img.shape[1]/img.shape[0]<1.9:
    img_resize = ResizeWithAspectRatio(img, height=600)
else: img_resize = ResizeWithAspectRatio(img, width=1200)



cv2.imshow('Original Image', img_resize)
cv2.waitKey(0)

