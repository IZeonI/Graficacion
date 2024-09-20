import cv2 as cv

cap=cv.VideoCapture(0)
while(True):
    ret, img = cap.read()
    if ret:
        cv.imshow('video', img)
        #azul=cv.cvtColor(img, cv.COLOR_BGR2RGB)
        #cv.imshow('azul',azul)
        #gris=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        #cv.imshow('gris', gris)
        #hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
        #cv.imshow('hsv',hsv)
        prueba=cv.cvtColor(img, cv.COLOR_BGR2XYZ)
        cv.imshow('prueba',prueba)
        #img3=255-img
        #cv.imshow('img3',img3)
        
        #w,h=gris.shape
        #for i in range(w):
        #    for j in range(h):
        #        gris[i,j]=255-gris[i,j]
        #cv.imshow('invertido',gris)
        
        k=cv.waitKey(1) & 0xFF
        if k==27:
            break
    else:
        break        
    
cap.release()
cv.destroyAllWindows()