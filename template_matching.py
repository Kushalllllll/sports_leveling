import cv2
import numpy as np
img_bgr = cv2.imread('nike-basketball.jpeg.jpg') 
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
template1 = cv2.imread('Basketball.jpeg.jpg')
template =cv2.cvtColor(template1, cv2.COLOR_BGR2GRAY)

w, h = template.shape[::-1]
res = cv2.matchTemplate (img_gray, template, cv2.TM_CCOEFF_NORMED) 
threshold = 0.45
loc = np. where (res >= threshold)
for pt in zip(*loc[::-1]): 
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

cv2.imshow('detected', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()