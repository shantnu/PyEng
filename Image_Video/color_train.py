#!/usr/bin/python
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from SimpleCV import *

# The location in the picture which only has the shirt.
# Format is: x, y, x_size, y_size
# I found the x , y positions by opening the file in Gimp.
shirt_location = (240,378,120,120)

def find_rgb(blobs):
    '''
    Find the RGB values in blobs of data. The fucntion loops over the blobs
    and finds the average of the rgb values
    
    Input: The output of the findBlobs() function
    Output: The average rgb values are returned.
    '''
    red, green, blue = 0,0,0
    for blob in blobs:
        colors = blob.meanColor()
        red += colors[0]
        green += colors[1]
        blue += colors[2]

    red = red / len(blobs)
    green = green / len(blobs)
    blue = blue / len(blobs)
    
    return red, green, blue
    
# Read the red and blue shirts
red = Image("red_train.jpg")
red2=red.crop(shirt_location)

# Warning: SimpleCv uses pygame, which is stupid.
# It will only exit when quit() is called.
# If your system freezes, don't panic, press enter.
show_im = red.show()
raw_input("Press Enter to continue")
show_im.quit()

show_im = red2.show()
raw_input("Press Enter to continue")
show_im.quit()

blue = Image("blue_train.jpg")
blue2=blue.crop(shirt_location)

# See the color
print(red2.meanColor()) #(41.038071895424835, 1.3220588235294117, 194.17328431372547)
print(blue2.meanColor()) #(171.3142973856209, 61.778431372549015, 24.947303921568626)

# Clearly not red enough! Let's read the ideal colors

red_ideal = Image("red_ideal.jpg")
red_ideal = red_ideal.crop(shirt_location)
# Pure red!
red_ideal.meanColor() #(0.058333333333333334, 0.0, 254.0)

blue_ideal = Image("blue_ideal.jpg")
blue_ideal = blue_ideal.crop(shirt_location)
# Pure red!
blue_ideal.meanColor()  #(254.0, 0.0, 0.008333333333333333)

# Find the different colored blobs
blob_red=red2.findBlobs()
blob_blue=blue2.findBlobs()

# Find rgb values
red, green, blue = find_rgb(blob_red)
print("The RGB values for the red shirt are: red {}  green {}  blue {}".format(red, green, blue))
# The RGB values for the red shirt are: red 200.841750984  green 1.5193715676  blue 43.4040374198


red, green, blue = find_rgb(blob_blue)
print("The RGB values for the blue shirt are: red {}  green {}  blue {}".format(red, green, blue))
# The RGB values for the blue shirt are: red 29.0385591969  green 64.2966580905  blue 173.929505814

