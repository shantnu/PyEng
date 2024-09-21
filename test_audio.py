from audio import get_freq,create_wave,noisy
import os
import math


def test_create_wave():
    try:
        for f in glob.glob("test.wav"):
            os.remove(f)
    except:
        pass
    create_wave.create_wav()
    assert(os.path.exists("test.wav"))

def test_get_freq():
    assert(1000 == get_freq.get_freq(True))

def test_noisy():
    a,b = noisy.noisy(True)
    tolerance = 0.1  


    assert math.isclose(a, 24000.0, rel_tol=tolerance), f"a={a} is not within tolerance of 24000.0"
    assert math.isclose(b, 1000.0, rel_tol=tolerance), f"a={a} is not within tolerance of 24000.0"
