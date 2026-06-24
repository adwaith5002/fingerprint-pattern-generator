import cv2
import numpy as np
img = np.zeros((500,500,3), np.uint8)
for i in range(20,220,8):
    cv2.ellipse(
        img,
        (250,250),
        (i,i//2),
        20,
        0,360,
        (0,255,255),
        1
    )

cv2.imshow("Fingerprint", img)
cv2.waitKey(0)
