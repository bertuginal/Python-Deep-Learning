import cv2
import numpy as np

img = cv2.imread("h_line.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)#cv2.Canny(resim, min deger, max deger) --> resimdeki köşeleri tespit eder.

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=200) #cv2.HoughLinesP(resim, row, teta, threshold degeri, enfazla çizgi boşluğu)-->çizgileri tespit eder
#cv2.HoughLines()--> CPU çok kullanır.cv2.HoughLinesP() tercih edilir.
print(lines)

for line in lines:#line'lar tek tek lines içinde dolaşır.
    (x1, y1, x2, y2) = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)#cv2.line(resim, başlangıc noktasi, bitis noktasi, renk, kalınlık)

cv2.imshow("Image", img)
cv2.imshow("Gray", gray)
cv2.imshow("Edges", edges)


cv2.waitKey(0)
cv2.destroyAllWindows()
