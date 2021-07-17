# This function will be executed before setup
def setup_module() -> None:
    print('Setting up Test Module!')


def teardown_module() -> None:
    print('Tearing Down Test Module!')

# This function will be executed before tests


def setup_function(func) -> None:
    if func == test1:
        print('Setting up test1!')
    elif func == test2:
        print('Setting up test2!')
    else:
        print('Setting up an unknown test!')

# This function will be executed after tests


def teardown_function(func) -> None:
    if func == test1:
        print('Tearing Down test1!')
    elif func == test2:
        print('Tearing Down test2!')
    else:
        print('Tearing Down an unknown test!')

# Unit test functions


def test1() -> None:
    print('Executing test1')
    assert True


def test2() -> None:
    print('Executing test2!')
    assert True
