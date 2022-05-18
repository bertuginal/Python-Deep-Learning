import cv2
import numpy as np

img =cv2.imread("star.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0) #0 yerine cv2.THRESH_BINARY de yazılabilir.

contours, ret = cv2.findContours(thresh, 2, 1)

cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull) # kusurları yani iç bükeyleri bulur

for i in range(defects.shape[0]): #range(defects.shape[0])-->0'dan kusurların boyutuna kadar
    s, e, f, d = defects[i, 0] #s->starpoint e->endpoint f->fartestpoint d->distance
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0, 255, 0], 2)
    cv2.circle(img, far, 5, [0, 0, 255], -1)


cv2.imshow("Gray", gray)
cv2.imshow("Thresh", thresh)
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
