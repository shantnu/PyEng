#!/usr/bin/python

from SimpleCV import *
import sys

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


# Get the shirt and crop it to the required location.    
shirt = sys.argv[1]
shirt = Image(shirt)
shirt = shirt.crop(shirt_location)

print(shirt.meanColor())
# Find rgb values
blob = shirt.findBlobs()
red, green, blue = find_rgb(blob)
print("The RGB values for the shirt are: red {}  green {}  blue {}".format(red, green, blue))

if (red > 150) and (blue < 70) and (green < 70):
    print("Found a red shirt")
elif (blue > 150) and (red < 70) and (green < 70):
    print("Found a blue shirt")
else:
    print("Unknown color")