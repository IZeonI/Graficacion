import numpy as np
import cv2

width, height= 1000,1000
img=np.ones((height,width,3), dtype=np.uint8)*255

a,b,c,d,j,k=1,4,4,1,3,3
theta_increment=0.05
max_theta=2*np.pi

center_x, center_y = width//2, height//2
theta=0

while True:
    img=np.ones((width,height,3), dtype=np.uint8)*255
    
    for t in np.arange(0,theta,theta_increment):
        x = int(center_x+200*np.cos(a * t) - (np.cos(b * t)) ** j)
        y = int(center_y+200*np.sin(c * t) - (np.sin(d * t)) ** k)
        
        cv2.circle(img,(x,y),1,(0,0,255),2)
        
        
    cv2.imshow("Paremetricaciones",img)
    theta+=theta_increment
        
            
    if cv2.waitKey(30) & 0xFF == 27:  
            break
cv2.destroyAllWindows()
        

        
        


