import cv2
import sys

# The first argument is the image
image = cv2.imread(sys.argv[1])

cv2.imshow("Image", image)
cv2.waitKey(0)