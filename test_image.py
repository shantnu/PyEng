from pdb import Pdb
from Image_Video import display,blur,edge_detect,count_cards,face_detect
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



def test_count_cards():
    try:
        for f in glob.glob("test*.png"):
            os.remove(f)
    except:
        pass
    image = "Image_Video/cards.jpg"
    cards = count_cards.count_cards(image, True)
    assert(cards == 5)
    assert(os.path.exists("test_count_cards.png"))
    for f in glob.glob("test*.png"):
        os.remove(f)

def test_face_detect():
    try:
        for f in glob.glob("test*.png"):
            os.remove(f)
    except:
        pass
    image = "Image_Video/abba.png"
    faces = face_detect.face_detect(image, True,  "Image_Video/haarcascade_frontalface_default.xml")
    assert(faces == 4)
    assert(os.path.exists("test_face.png"))
    for f in glob.glob("test*.png"):
        os.remove(f)


TODO test for webcam face detect, dont know if can test motion deetct