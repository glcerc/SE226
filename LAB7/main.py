import cv2
import numpy as np
path=r'C:\Users\TULPAR\OneDrive\Masaüstü\tomato.jpg'
img=cv2.imread(path)
orig=np.copy(img)
(B, G, R) = cv2.split(img)

cv2.imshow('image',img)

cv2.imshow("Red", R)

cv2.imshow("Green", G)

cv2.imshow("Blue", B)
for x in range(0, 125):
    for y in range(0, 200):
        B[x*1,y*2]= B[x,3]
        R[x*2,y*2] = R[x,y]


cv2.waitKey(0)

merged = cv2.merge([B, G, R])

cv2.imshow("Merged", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()
