import cv2
import sys

# Read the image
image = cv2.imread(sys.argv[1])

#convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blur it
blurred_image = cv2.GaussianBlur(gray_image, (7,7), 0)

# Show both our images
cv2.imshow("Original image", image)
cv2.imshow("Blurred image", blurred_image)

# Run the Canny edge detector
canny = cv2.Canny(blurred_image, 30, 100)
cv2.imshow("Canny", canny)

contours, hierarchy = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Number of objects found = ", len(contours))

objects = image.copy()
cv2.drawContours(objects, contours, -1, (0,255,0), 2)
cv2.imshow("objects Found", objects)
cv2.waitKey(0)