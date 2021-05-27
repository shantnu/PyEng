from pdb import Pdb
from Image_Video import display,blur,edge_detect
import os
import glob

def test_display():
    try:
        for f in glob.glob("test*.png"):
            os.remove(f)
    except:
        pass
    image = "Image_Video/ship.jpg"
    display.display(image, True)
    assert(os.path.exists("test_display2.png"))


def test_blur():
    try:
        for f in glob.glob("test*.png"):
            os.remove(f)
    except:
        pass
    image = "Image_Video/ship.jpg"
    blur.blur_display(image, True)
    assert(os.path.exists("test_blurred.png"))

def test_edge():
    try:
        for f in glob.glob("test*.png"):
            os.remove(f)
    except:
        pass
    image = "Image_Video/ship.jpg"
    edge_detect.edge_detect(image, True)
    assert(os.path.exists("test_edge.png"))



    for f in glob.glob("test*.png"):
        os.remove(f)