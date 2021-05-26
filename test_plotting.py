from Plotting import list_comp

def test_list_comp():
    data = list_comp.main()
    print(data)
    assert(data.strip("\n") == 'With Numpy: a = [ 5 10 15 20 25] b = [1. 2. 3. 4. 5.] ')
