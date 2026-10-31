import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread("images.jpeg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
(h,w)= image.shape[:2]
centre =(w//2,h //2)
M=cv2.getRotationMatrix2D(centre,45,1.0)
rotated_image=cv2.warpAffine(image_rgb,M,(w,h))
rotated_image_rgb=cv2.cvtColor(rotated_image,cv2.COLOR_BGR2RGB)
plt.imshow(rotated_image_rgb)
plt.title("Rotated image")
plt.show()
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brightened_image = cv2.add(image, brightness_matrix)
brighter_image_rgb = cv2.cvtColor(brightened_image, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_image_rgb)
plt.title("Brightened image")
plt.show()