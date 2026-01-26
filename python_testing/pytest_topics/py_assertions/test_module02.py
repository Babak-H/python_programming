class TestMyStuffSuite:

    def test_type(self):
        assert type(1) == int
        assert type(1.5) == float


    def test_strs(self):
        assert str.upper('python') == 'PYTHON'
        assert 'pytest'.capitalize() == 'Pytest'