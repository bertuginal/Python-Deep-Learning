import cv2

# video dosyası
cap = cv2.VideoCapture("antalya.mp4")


while True:
    ret, frame = cap.read()
    # frame = cv2.flip(frame, 1) --> videoyu ters döndürür, aslında frame'ler ters döndürülür.
    if ret == 0:
        break


    cv2.imshow("Antalya", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release() #--> bu kod ile kapatmazsak başka uygulama da başka işlem yapılmaz.
cv2.destroyAllWindows()