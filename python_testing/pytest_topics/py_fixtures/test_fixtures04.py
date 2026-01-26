import pytest

months = ["Jan", "Feb", "Mar"]


def test_check_request(setup04):
    assert "April" in setup04
    assert len(setup04) == 4

def test_factory_fixture(setup05):
    assert type(setup05('list')) == list
    assert type(setup05('tuple')) == tuple