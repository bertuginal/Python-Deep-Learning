import cv2

#RESİM OKUMA
img = cv2.imread("D:\Pycharm\klon.jpg",0) #--> 0 demek resmi gri yapar.
# # print(img)

#RESİM GÖSTERME
cv2.namedWindow("klon",cv2.WINDOW_NORMAL) # --> cv2.WINDOW_NORMAL komutu resmi boyutlandırmamızı sağlar.
cv2.imshow("klon",img) #--> resmi gösterir.
cv2.waitKey(0) #--> açılıp kapanmasını önler. Hep açık kalır
cv2.destroyAllWindows() #--> pencereyi kapatmamızı sağlar.

#RESİM KAYDETME
cv2.imwrite("D:\Pycharm\Projelerim\klon.jpg",img) #--> resmi nereye kaydetmek istersek lokasyonunu yazarız.
