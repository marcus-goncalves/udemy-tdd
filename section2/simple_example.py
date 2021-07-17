# A Production function
def str_len(the_string: str) -> int:
    return len(the_string)

# A Unit Test


def test_str_len():
    # Initialization or Setup
    test_str = "Hello World!"

    # Execution or Action
    result = str_len(test_str)

    # Validation or Assert
    assert result == 12
