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


def fizz_buzz(number: int):
    return


def test_canCallFizzBuzz():
    fizz_buzz(1)


def test_return1With1PassedIn():
    result = fizz_buzz(1)
    assert result == "1"
