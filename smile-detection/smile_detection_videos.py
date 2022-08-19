import cv2


vid = cv2.VideoCapture("smile.mp4")

face_cascade = cv2.CascadeClassifier('frontalface.xml')
smile_cascade = cv2.CascadeClassifier('smile.xml')

while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_frame = frame[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.9, 3)

        for (ex, ey, ew, eh) in smiles:
            cv2.rectangle(roi_frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 3)

    cv2.imshow('Smile Capture', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()   
