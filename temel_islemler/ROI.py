# ROI --> Region Of Interest --> İlgi Alanı
import cv2
import numpy as np

img = cv2.imread("klon.jpg")
# print(img.shape) --> Resmin boyutunu gösterir.

roi = img[30:200, 200:400]

cv2.imshow("Klon Asker", img)
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()