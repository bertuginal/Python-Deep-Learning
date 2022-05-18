import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255 #--> np.uint8 = çizim yağtığımızda kullandığımız veri tipidir.
#print(canvas)                                        # +255 demek renk vermek demektir. Matrislerin değerini değiştirir.

#çizgi oluşturma
cv2.line(canvas, (50,50),(512,512),(255,0,0),thickness=5) #--> thickness=çizgi kalınlığı. Sadece numarayı yazsak da olur
cv2.line(canvas, (100,50),(200,250),(0,0,250),thickness=7) # ilk parantez başlangıç nokt. 2. parantez bitiş nokt. 3. parantez renk

#dikdörtgen-kare oluşturma
cv2.rectangle(canvas,(20,20), (50,50),(0,255,0), thickness=-1) #--> dikdörtgen oluşturur. thickness=-1 girmek içini doldurur.
cv2.rectangle(canvas,(50,50), (150,150),(0,255,0), thickness=-1)

#çember-daire oluşturma
cv2.circle(canvas,(250,250),100,(0,0,255), thickness=5)
cv2.circle(canvas,(350,350),100,(0,0,255), thickness=-1)

#üçgen oluşturma ==> özel bir fonksiyonu yoktur. line fonksiyonu ile üçgen oluşturulur.
p1 = (100,200)
p2 = (50,50)
p3 = (300,100)

#yamuk oluşturma
points = np.array([[[110,200], [330,200],[290,220],[100,100]]],np.int32)
cv2.polylines(canvas, [points], True, (0,0,100), 5) #True yapmak çizgileri tamamlar.

#elips oluşturma
cv2.ellipse(canvas, (300,300), (100,35), 0, 0, 360, (255,255,0), -1)

cv2.line(canvas,p1,p2,(0,0,0),4)
cv2.line(canvas,p2,p3,(0,0,0),4)
cv2.line(canvas,p3,p1,(0,0,0),4)



cv2.imshow("Canvas", canvas)
cv2.waitKey()
cv2.destroyAllWindows()

