import pytest
import sys

# can skip whole module's tests based on given condition
# pytestmark = pytest.mark.skipif(sys.platform == 'win32', reason='runs on linux OS only')

CONST = 9/5


def cent_to_fah(cent=0):
    fah = (cent * CONST) + 32
    return fah

print(cent_to_fah(-18))

@pytest.mark.skip("skipping for no reason at all")
def test_case01():
    assert type(CONST) == float

@pytest.mark.skipif(sys.version_info > (3, 6), reason="does not work on higher versions of python")
def test_case02():
    assert cent_to_fah() == 32

@pytest.mark.skipif(pytest.__version__ < '9.0.0', reason="cant run lower than pytest version 9")   # '9.0.2'
def test_case03():
    assert cent_to_fah(38) == 100.4

@pytest.mark.skipif(cent_to_fah() == 32, reason="default value already tested!")
def test_case04():
    assert cent_to_fah() == 32