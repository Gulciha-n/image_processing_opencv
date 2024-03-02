import cv2
import numpy as np

img = cv2.imread("Football.png",0)
ret , th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#cv2.imshow("image",img)
cv2.imshow("img.th1",th1)

cv2.waitKey(0)
cv2.destroyAllWindows()



