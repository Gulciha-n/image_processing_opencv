import cv2

img = cv2.imread("contour.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  # görseli ikilik sisteme çevirdik

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #contour koordinatlarıını bulduk

cnt = contours[0]
area = cv2.contourArea(cnt)
print(area)

perimeter = cv2.arcLength(cnt,True)  # True = şeklin kapalı ve açık olma durumunu ifade eder.
print(perimeter)

cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

