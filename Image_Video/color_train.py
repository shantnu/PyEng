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

blue = Image("blue_train.jpg")
blue2=blue.crop(shirt_location)

# Find the different colored blobs
blob_red=red2.findBlobs()
blob_blue=blue2.findBlobs()

# Find rgb values
red, green, blue = find_rgb(blob_red)
print("The RGB values for the red shirt are: red {}  green {}  blue {}".format(red, green, blue))

red, green, blue = find_rgb(blob_blue)
print("The RGB values for the blue shirt are: red {}  green {}  blue {}".format(red, green, blue))