import cv2 as cv
import numpy as np

img=np.ones((500,500), dtype=np.uint8)*255
cv.circle(img,(0,0),50,(0,234,21), -1)
cv.line(img,(20,20),(230,240),(0,234,21), 3)
cv.rectangle(img,(0,0),(200,200),(0,234,21),3)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()