from Pandas import obesity,pandas_movie

def test_obseity():
    value = obesity.obesity("Pandas/Obes-phys-acti-diet-eng-2014-tab.xls", True)
    assert(value == 1711.0)

def test_movie():
    assert(pandas_movie.movie(True,"Pandas/") == 0.6127323258641648)
