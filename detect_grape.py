import cv2
import numpy as np 
from google.colab.patches import cv2_imshow

original = cv2.imread('grape-1.jpg')

# Convert image in grayscale
gray_im = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray_im)
gray_correct = np.array(255 * (gray_im / 255) ** 1.2 , dtype='uint8')
thresh = cv2.adaptiveThreshold(gray_correct, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 19)
thresh = cv2.bitwise_not(thresh)
cv2_imshow(thresh)
# Dilatation et erosion
kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
img_erode = cv2.erode(img_dilation,kernel, iterations=1)
# clean all noise after dilatation and erosion
img_erode = cv2.medianBlur(img_erode, 7)
cv2_imshow(img_erode)

ret, labels = cv2.connectedComponents(img_erode)
label_hue = np.uint8(179 * labels / np.max(labels))
blank_ch = 255 * np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
labeled_img[label_hue == 0] = 0
cv2_imshow(labeled_img)
print('Grape count:', ret-1)
