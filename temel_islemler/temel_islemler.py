import cv2
import numpy as np

img = cv2.imread("klon.jpg")
dimension = img.shape
print(dimension)

color = img[420, 500]
print("BGR: ", color)

blue = img[420, 500, 0]
print("Blue: ", blue)

green = img[420, 500, 1]
print("Green: ", green)

red = img[420, 500, 2]
print("Red: ", red)

#Renk değiştirme
img[420, 500, 0] = 250 # mavi değeri 140 iken artık 250 oldu.
print("New Blue: ", img[420, 500, 0])

color1 = img[150, 200]
print("BGR: ", color1)

blue1 = img.item(150, 200, 0)
print("blue1: ",blue1)
img.itemset((150, 200, 0), 172)
print("New blue1: ", img[150, 200, 0])

cv2.imshow("Klon Asker", img)
cv2.waitKey(0)
cv2.destroyAllWindows()