import cv2

img = cv2.imread("contour1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)#(gray, max deger, min deger, siyah ya da beyaz olacağını gösterir.)
contours, ret=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#--> cv2. olan argümanlar yaptığımız işlemleri kolaylaştırır
# print(contours) --> koordinatları gösterir.

cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
cv2.imshow("Contour", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

