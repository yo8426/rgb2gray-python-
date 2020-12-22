import numpy as np
import cv2

im=cv2.imread('1.jpg')
im=np.array(im,dtype='double')

im_gray=im[:,:,2]*0.299+im[:,:,1]*0.587+im[:,:,0]*0.114
im_gray=np.array(im_gray,dtype='uint8')

cv2.imwrite('1_gray.jpg',im_gray)
