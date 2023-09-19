from calculator import subtract, multi, addition_route

def test():
    assert 0 == subtract(2,2)
    assert 4 == multi(2,2)
    assert 4 == addition_route(2,2)
