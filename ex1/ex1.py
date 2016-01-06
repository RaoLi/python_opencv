# import numpy as np
# import cv2
# 
# img = cv2.imread('1.jpg',3)
# 
# 
# cv2.imwrite('clone',img)
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
# cv2.waitKey(1000)
# cv2.destroyAllWindows()

import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0) 
while(True):
# Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()