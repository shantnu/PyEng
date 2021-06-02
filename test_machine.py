from machine import calc_correlation,ml_main

def test_calc_corr():
    corr_dict = calc_correlation.main("machine/ml_data1.py")
    assert (corr_dict['Terminator']['Terminator 2'] == 0.9986154372037583)


def test_ml_main():
    rec = ml_main.main()
    assert rec['Terminator 2'] == 4.010450484453663