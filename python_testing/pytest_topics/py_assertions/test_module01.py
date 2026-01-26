def test_a1():
    assert 4 <= 5


def test_a2():
    assert 3 != 10


def test_a3():
    assert 1
    # assert True


def test_a4():
    assert False


def test_a5():
    assert "abcd" == 'abcd'


def test_a6():
    assert (3-1*4/2) == 4  # 1
    # ((3-1)*(4/2))


def test_a7():
    assert divmod(10, 3) == (3, 1)
    # while not recommended, we can have several asserts in one pytest function
    assert 3 in divmod(10, 3)
    assert 'py' in 'this is pytest'
    assert 5 in [1, 2, 3, 4, 5]