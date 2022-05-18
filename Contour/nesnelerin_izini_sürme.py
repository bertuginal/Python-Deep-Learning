import cv2
import numpy as np

cap = cv2.VideoCapture("dog.mp4")

while 1: # 1 de yazsak True da yazsak sonsuz döngü oluşturur.

	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	sensitivity = 15
	lower_white = np.array([0, 0, 255-sensitivity]) # hsv code for white olarak google dan arat (hangi renk için uygulamak istersek onun için) ve değerleri bul.
	upper_white = np.array([255, sensitivity, 255])

	mask = cv2.inRange(hsv, lower_white, upper_white) # cv2.inRange() --> lower ve upper white olanları kullan ve geri kalanını sil,kazı
	res = cv2.bitwise_and(frame, frame, mask=mask) #özel bir kullanımdır. Kullanmak zorunlu.
	
	cv2.imshow("frame", frame)
	cv2.imshow("mask", mask)
	cv2.imshow("result", res)
	
	k = cv2.waitKey(5) & 0xFF #ESC basınca bütün pencereleri kapatır
	if k == 27:
		break

cv2.destroyAllWindows()