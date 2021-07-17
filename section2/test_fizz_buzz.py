"""
USE CASES:
- Call FizzBuzz function
- Get "1" when 1 is passed
- Get "2" when 2 is passed
- Get "Fizz" when 3 is passed
- Get "Buzz" when 5 is passed
- Get "Fizz" when a multiple of 3 is passed (6)
- Get "Buzz" when a multiple of 5 is passed (10)
- Gut "FizzBuzz" when a multiple of 3 and 5 is passed (15)
"""
# Support Functions


def check_fizz_buzz(val: int, expected: str) -> None:
    result = fizz_buzz(val)
    assert result == expected


def is_multiple(val: int, mod: int) -> bool:
    return val % mod == 0


# FUNCTION TO BE TESTED
def fizz_buzz(number: int) -> str:
    if is_multiple(number, 3) and is_multiple(number, 5):
        return "FizzBuzz"

    if is_multiple(number, 3):
        return "Fizz"

    if is_multiple(number, 5):
        return "Buzz"

    return str(number)


# UNIT TEST FUNCTIONS
def test_return1With1PassedIn() -> None:
    check_fizz_buzz(1, "1")


def test_return2With2PassedIn() -> None:
    check_fizz_buzz(2, "2")


def test_returnFizzWith3PassedIn() -> None:
    check_fizz_buzz(3, "Fizz")


def test_returnBuzzWith5PassedIn() -> None:
    check_fizz_buzz(5, "Buzz")


def test_returnFizzWith6PassedIn() -> None:
    check_fizz_buzz(6, "Fizz")


def test_returnFizzWith10PassedIn() -> None:
    check_fizz_buzz(10, "Buzz")


def test_returnFizzBuzzWith15PassedIn() -> None:
    check_fizz_buzz(15, "FizzBuzz")
