from studentdb import StudentDB
import pytest

'''
when you try to test real databases (mysql, postgres,..) you can use same approach
'''
db = None


# setup_module for pytest is similar to init for normal python classes, it will run before any other function in the test module
def setup_module(module):
    global db
    db = StudentDB()
    db.connect('data.json')


# this function will free the resources at the end of testing process
def teardown_module(module):
    db.close()


def test_scott_data():
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'


def test_mark_data():
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'


@pytest.mark.parametrize('idx, name, result', [(1, 'Scott', 'pass'), (2, 'Mark', 'fail')])
def test_data(idx, name, result):
    data = db.get_data(name)

    assert data['id'] == idx
    assert data['name'] == name
    assert data['result'] == result
