import cv2

cv2.namedWindow("Klon")
img = cv2.imread("klon.jpg")
img = cv2.resize(img, (640,480))

cv2.imshow("Klon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
