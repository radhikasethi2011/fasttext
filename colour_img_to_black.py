import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt
import os
import time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",type=str, required=True,
	help="path to input image file")
args = vars(ap.parse_args())
 
# load the image from disk
image = cv2.imread(args["image"])
image = cv2.medianBlur(image,5)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
th3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,11,2)

images = [th3]

for i in range(1):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    
    plt.xticks([]),plt.yticks([])
plt.show()

neg_4 = time.strftime("%Y_%m_%d-%H:%M:%S") + '.png'
ret = cv2.imwrite(os.path.join(neg_4), image)
print(ret)
