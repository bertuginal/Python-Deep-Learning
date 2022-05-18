import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

fileName = "D:\Pycharm\Projelerim\webcam.avi" #--> nereye kaydedileceğini gösteririz.
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2') #--> codec ses ve görüntü kodlarını çözümler.
frameRate = 30 #--> frame oranı
resolution = (640, 480) #--> video çözünürlüğü

videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    videoFileOutput.write(frame)

    cv2.imshow("Webcam Live", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoFileOutput.release() #--> videoyu serbest bırakır.
cap.release()
cv2.destroyAllWindows()