import cv2
import numpy as np

img = np.zeros((800, 600, 3), np.uint8)

for i in range(20, 220, 8):

    # Shift center gradually
    cx = 300 + i // 4
    cy = 400

    cv2.ellipse(
        img,
        (cx, cy),
        (i, int(i * 1.4)),
        0,
        0,
        360,
        (255, 100, 0),
        2
    )

cv2.imshow("Fingerprint", img)
cv2.waitKey(0)
cv2.destroyAllWindows()