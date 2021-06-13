import cv2
import numpy as np
from numpy.core import einsumfunc

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
image = cv2.VideoCapture(0)

bg = 0
for i in range(60):
    ret,bg = image.read()
while():
    frame = cv2.resize(frame, (640,480))
    image = cv2.resize(image, (640,480))

    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])

    mask = = cv2.inRange(frame,l_black,u_black)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    inRange(u_black,l_black)

    np.where(
        f = frame - res
        f = np.where(f == 0,image, f)
            )
        
    if not res :
        break('esc','q')

image.release()
cv2.destroyAllWindows()
