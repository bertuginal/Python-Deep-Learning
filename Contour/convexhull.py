import cv2
import numpy as np

img = cv2.imread("map.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #siyah-beyaz'a dönüştürür. Aslında 0-1 çevirmek demektir.
blur = cv2.blur(gray, (3, 3))
ret, thresh = cv2.threshold(blur, 40, 255, cv2.THRESH_BINARY) # thresh-->daha da siyah beyaz eder, sıyırır.

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = []

for i in range(len(contours)): # range(len(contours))--> 0 dan contoursun uzunluğuna kadar olan sayıları döndürür
    hull.append(cv2.convexHull(contours[i], False)) # hull.append--> değerleri boş diziye atar.

bg = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8) #np.zeros--> siyah bir ekran oluşturur. 3-->renkli çizim için.

for i in range(len(contours)):
    cv2.drawContours(bg, contours, i, (0, 255, 0), 3, 8)
    cv2.drawContours(bg, hull, i, (0, 0, 255), 1, 8)


cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Thresh", thresh)
cv2.imshow("Image", bg)


cv2.waitKey(0)
cv2.destroyAllWindows()
