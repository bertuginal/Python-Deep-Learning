import cv2
import numpy as np
import  requests

url = "http://192.168.1.254:8080//shot.jpg" #--> IP Webcam uygulamasından bir sunucu oluşturduk ve bir frame URL'sini aldık.

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) #--> hafızadan aldığımız görüntüyü tekrar çeker ve video haline getirir.
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR) #--> hafızadan çektiğimiz görüntüyü görüntülenebilir hale getirir ve renklendirir.
    img = cv2.resize(img,(640, 480)) #--> kameranın boyutunu ayarlar.

    cv2.imshow("Android Camera", img)
    if cv2.waitKey(1) == 27: #--> ESC ye basınca sonlanır. Uzun kodun kısası..
        break

cv2.destroyAllWindows()