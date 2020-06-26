import pytest

@pytest.fixture()
def setup():
    print("learning")

def test_methoda(setup):
    print("method1")

def test_methodb(setup):
    print("method2")