import cv2
import sys

def edge_detect(infile, nogui=False):
# The first argument is the image
    image = cv2.imread(infile)

    #conver to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #blur it
    blurred_image = cv2.GaussianBlur(gray_image, (7,7), 0)
    # Use low thresholds
    canny = cv2.Canny(blurred_image, 10, 30)
    # Use high thresholds
    canny2 = cv2.Canny(blurred_image, 50, 150)

    if nogui:
        cv2.imwrite('test_edge.png', canny2)
    else:
        cv2.imshow("Orignal Image", image)
        cv2.imshow("Canny with low thresholds", canny)
        cv2.imshow("Canny with high thresholds", canny2)
        cv2.waitKey(0)

if __name__ == "__main__":
    edge_detect(sys.argv[1])