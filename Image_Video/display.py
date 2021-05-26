import cv2
import sys


def display(infile, nogui=False):
    image = cv2.imread(infile)
    if nogui:
        cv2.imwrite('test_display2.png', image)
    else:
        cv2.imshow("Image", image)
        cv2.waitKey(0)

if __name__ == "__main__":
    # Read the image. The first command line argument is the image

    display(sys.argv[1])