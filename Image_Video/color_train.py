#!/usr/bin/python


import cv2

# The location in the picture which only has the shirt.
# Format is: x, y, x_size, y_size
# I found the x , y positions by opening the file in Gimp.
shirt_location = (240,378,120,120)


def find_rgb(blobs):
    '''
    Find the RGB values in blobs of data. The function loops over the blobs
    and finds the average of the rgb values
    
    Input: The output of the findBlobs() function
    Output: The average rgb values are returned.
    '''
    red, green, blue = 0,0,0
    for blob in blobs:
        colors = cv2.mean(blob)
        red += colors[0]
        green += colors[1]
        blue += colors[2]

    red = red / len(blobs)
    green = green / len(blobs)
    blue = blue / len(blobs)
    
    return red, green, blue
    
# Read the red and blue shirts
red = cv2.imread("red_train.jpg")
red2 = red[378:498, 240:360]

cv2.imshow("red ", red)
input("Press Enter to continue")
cv2.waitKey(0)


cv2.imshow("red cropped", red2)
input("Press Enter to continue")
cv2.waitKey(0)


blue = cv2.imread("blue_train.jpg")
blue2=blue[378:498, 240:360]

# See the color
print(cv2.mean(red2)) #(41.038071895424835, 1.3220588235294117, 194.17328431372547)
print(cv2.mean(blue2)) #(171.3142973856209, 61.778431372549015, 24.947303921568626)

# Clearly not red enough! Let's read the ideal colors


red_ideal = cv2.imread("red_ideal.jpg")
red_ideal = red_ideal[378:498, 240:360]
# Pure red!
cv2.mean(red_ideal) #(0.058333333333333334, 0.0, 254.0)

blue_ideal = cv2.imread("blue_ideal.jpg")
blue_ideal = blue_ideal[378:498, 240:360]

# Pure blue!
cv2.mean(blue_ideal)  #(254.0, 0.0, 0.008333333333333333)

#blob params

params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 0;
params.maxThreshold = 256;



# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create(params)

# Find the different colored blobs
blob_red= detector.detect(red2)
blob_blue=detector.detect(blue2)

print('blob_red ', blob_red, blob_blue)
# Find rgb values
red, green, blue = find_rgb(blob_red)
print("The RGB values for the red shirt are: red {}  green {}  blue {}".format(red, green, blue))
# The RGB values for the red shirt are: red 200.841750984  green 1.5193715676  blue 43.4040374198


red, green, blue = find_rgb(blob_blue)
print("The RGB values for the blue shirt are: red {}  green {}  blue {}".format(red, green, blue))
# The RGB values for the blue shirt are: red 29.0385591969  green 64.2966580905  blue 173.929505814


