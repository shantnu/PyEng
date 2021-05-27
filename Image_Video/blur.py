import cv2
import sys

def blur_display(infile, nogui=False):
    # The first argument is the image
    image = cv2.imread(infile)

    #conver to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #blur it
    blurred_image = cv2.GaussianBlur(image, (7,7), 0)

    if nogui:
        cv2.imwrite('test_blurred.png', blurred_image)
    else:

        # Show all 3 images
        cv2.imshow("Original Image", image)
        cv2.imshow("Gray Image", gray_image)
        cv2.imshow("Blurred Image", blurred_image)

        cv2.waitKey(0)

if __name__ == "__main__":
    blur_display(sys.argv[1])