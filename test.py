import numpy as np 
import cv2
import pandas as pd
import screeninfo

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

img = cv2.imread('B1.jpg')

print(type(img))

if img.shape[0]>img.shape[1] or img.shape[1]/img.shape[0]<1.9:
    img_resize = ResizeWithAspectRatio(img, height=600)
else: img_resize = ResizeWithAspectRatio(img, width=1200)

hsv_img = cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)

# lower range of red color in HSV
lower_range = (5, 100, 100)

# upper range of red color in HSV
upper_range = (15, 255, 255)
mask = cv2.inRange(hsv_img, lower_range, upper_range)
color_image = cv2.bitwise_and(img_resize, img_resize, mask=mask)

OrangePercentage = round(100*np.count_nonzero(mask)/mask.size,2)
print("orange percentage = " + str(OrangePercentage) +"%")

i=0
NonZ = np.zeros(mask.shape[0])
for row in mask:
    NonZ[i] = 100*np.count_nonzero(mask[i])/mask[i].size
    i = i+1

print(100*np.count_nonzero(NonZ > 20)/NonZ.size)

DF = pd.DataFrame(NonZ)
DF.to_csv("data1.csv")

# Display the color of the image
cv2.imshow('Original Image', img_resize)
cv2.imshow('Masked Image', mask)
cv2.imshow('Coloured Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
