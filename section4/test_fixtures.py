import pytest


"""
If you pass "autouse=True", every test use it without decorator
If you pass "scope=..." will set when the fixture will be scoped
Inside the function, if you use 'yield', every code after will be
a teardown function

"""


@pytest.fixture()
def setup() -> None:
    print('\nSetup!')
    yield
    print('\nTeardown!')


@pytest.mark.usefixtures('setup')
def test1() -> None:
    print('Executing test1 with fixture!')
    assert True


def test2() -> None:
    print('Executing test2 without Fixture!')
    assert True
