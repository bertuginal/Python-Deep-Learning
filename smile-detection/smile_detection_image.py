import cv2

img = cv2.imread("smile.jpg")

smile_cascade = cv2.CascadeClassifier("smile.xml")
face_cascade = cv2.CascadeClassifier("frontalface.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_img = img[y:y+h, x:x+w]
    smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 8)

    for (ex, ey, ew, eh) in smiles:
        cv2.rectangle(roi_img, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

cv2.imshow("Smile Capture", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

