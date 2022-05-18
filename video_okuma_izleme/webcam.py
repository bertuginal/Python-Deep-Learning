import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #--> webcam için 0 kullanılır. Hata alınıyorsa CAP_DSHOW kullanılır.

while True:
    ret, frame = cap.read() #--> eğer cap değişkeni frame'leri okuduysa ret değişkeninin değeri True'dur.
    frame = cv2.flip(frame, 1) #--> webcamden her bir frame'in yönü döndürülür. Ayna yansımasından kaçılır.
    if ret == 0:
        break

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): #--> "q" ya basınca uygulamayı sonlandırmaya yarar.
        break

cap.release() #--> bu kod ile kapatmazsak başka uygulama da başka işlem yapılmaz.
cv2.destroyAllWindows()