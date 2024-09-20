import cv2 as cv
import numpy as np

img=np.ones((500,500), dtype=np.uint8)*255

cv.rectangle(img,(250,250),(500,500),(0,23,255),-1)


cv.circle(img,(0,0),50,(0,234,21), -1)
cv.line(img,(20,20),(250,250),(0,234,21), 2)
cv.rectangle(img,(0,0),(250,250),(0,234,21),3)
cv.circle(img,(250,250),30,(0,234,21), -1)

cv.circle(img,(500,500),50,(255,254,21), -1)
cv.line(img,(500,500),(250,250),(255,254,21), 2)
cv.rectangle(img,(500,500),(250,250),(255,254,21),3)
cv.rectangle(img,(250,250),(0,500),(0,23,255),-1)

cv.circle(img,(250,250),10,(250,254,21), -1)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()