import pytest
from Pytest_topics.utils.myconfigparser import ConfigFileParser


@pytest.fixture()
def setup_src():
    return ConfigFileParser('prod.ini')

def test_get_gmail_url(setup_src):
    assert setup_src.get_gmail_user() == "gmail_prod_user1"