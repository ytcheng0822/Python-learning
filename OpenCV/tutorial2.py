import cv2
import numpy as np
import random

img = cv2.imread('colorcolor.jpg')
# print(img.shape)

# img = np.empty((300, 300, 3), np.uint8)

# for row in range(300):
#     for col in range(300):
#         img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]   # [B, G, R]

new_img = img[:150, :400]

cv2.imshow('img', img)
cv2.imshow('new_img', new_img)

cv2.waitKey(0)