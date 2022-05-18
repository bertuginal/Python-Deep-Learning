# 1. Kullanacağımız kütüphaneyi çalışmamıza dahil edelim.
import cv2

# 2. Kullanacağımız resmi çalışmamıza dahil edelim.
img = cv2.imread("face.png")

# 3. Kullanacağımız cascade dosyasını çalışmamıza dahil edelim.
face_cascade = cv2.CascadeClassifier("frontalface.xml")

# 4. Haar-like özellikleri kolay algılayabilmek için resmimizi boz(gri) tonlara çevirelim.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 5. Şimdi de cascade dosyamızı kullanarak resim üzerindeki yüzlerin koordinarlarını bulalım. (Birden fazla yüz olabilir bü yüzden bu komutu kullandık.)
faces = face_cascade.detectMultiScale(gray, 1.3, 7)

# 6. "faces" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
for (x, y, w, h) in faces: #x,y=sol ve üst w=yükseklık h=genişlik
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2) #(resim,sol üst koordinat, sağ alt koordinat, renk, kalınlık)

# 7. İşlediğimiz resmi görelim.
cv2.imshow('image', img)

# 8. Son olarak programı kapatacak kodu yazalım.
cv2.waitKey(0)
cv2.destroyAllWindows()
