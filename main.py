import cv2
import numpy as np
from matplotlib import pyplot as plt #importing matplot librabry
img = cv2.imread("traffic1.jpg", cv2.IMREAD_GRAYSCALE) #read test img
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3) #apply laplacian operator of ksize 3
lap = np.uint8(np.absolute(lap)) #using numpy to take max value of lap and convert into 8 bit
integer
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) #for sobel in x direction with dx first derivative
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1) #for sobel in y dir with dy first derivative
sobelX = np.uint8(np.absolute(sobelX)) #numpy data conversion
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY) #convolution of sobel x and y
canny = cv2.Canny(image=img, threshold1=100, threshold2=200) #canny edge detection
titles = ['image', 'Laplacian', 'sobelCombined', 'canny']
images = [img, lap, sobelCombined, canny]
for i in range(4):
plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray') #creating a 2 by 2 subplot as in matlab
plt.title(titles[i])
plt.xticks([]),plt.yticks([])
plt.show()