# udemy-tdd
Unit testing and TDD with python - Udemy Course
### Libs
pip install pytest
To run the tests use: pytest -v "name of the file"

## Section 2
### Why do we unit test?
* Software bugs hurt the business
* Software testing catches the bugs before they get to the field
* Need several levels of safety tests

### Levels of Testing
* Uni Testing - Function Level
* Component Testing - At the library and compiled binary level
* System Testing - external interfaces of a system
* Performance Testing - Verify timing and resources usages are acceptable

### Unit Testing Specifics
* Tests individual functions
* A test should be weitten for each test case for a function
* Groups of test can be combined into test suites for better organization
* Executes in the dev environment
* Execution of the tests should be automated

### What is TDD?
* A process where the dev takes personal responsability for the quality of their code
* Unit tests are written _before_ the production code
* Tests and production code are both written together, in small bits of functionality

### Benefits of TDD
* Gives you confidence to change code
* Gives you immediate feedback
* Documents what the code does
* Drives good objet oriented design

### TDD Workflow
* __RED__ Phase: Write a failing unit test
* __GREEN__ Phase: Write just enough code to make that test pass
* __REFACTOR__ Phase: refactor unit test and the production code to make it clean
* Repeat until the feature is complete

### Summary
* Unit tests are the first safety net for catching bugs
* Unit tests validate test cases for individual functions
* Unit tests should run fast
* Unit test should build and run only in DEV environment

## Section 4 Pytest Overview

### What is it?
* Unit Test Framework
* Privder ability to create Tests, Test Modules and Fixtures
* Uses built-in assert statement
* Has cmd line params to help filter which tests are executed and in what order

### Creating a Test
* Functions that starts with "test_"
* Similar test can be grouped together by including them in the same module or class

### Test Discovery
* Pytest will automatically discover tests when you execute it
* Classes name should start with "Test" and no have an "init" method
* Functions should start with "test_"

### Setup and Teardown functions
* It will execute code before and after test modules, test functions, test classes

### Fixtures
* Allow reuse of setup and teardown code accross tests
* Usage as a decorator "@pytest.fixture"

### Fixtures Scopes
* __Function__: Run once for each test
* __Class__: Run once for each class of tests
* __Module__: Run once when the module goes in scope
* __Session__: Run once pytest starts

### Assert Statements
* Asserting floats, use _approx_ from pytest
* For test exceptions, use _with raises_

## Section 6 - Unit Test Isolation with Dummies, Fakes, Stubs, Spies and Mocks

### What are Test Doubles
* Objects that are used as replacements to the real prod system collaborators

### Types of Doubles
* __Dummy__: Like placeholders, do not have any type of test implementation
* __Fake__: Simplified functional implementation of a particular interface
* __Stubs__: Provide implementations with canned answers that are suitable for the test
* __Spies__: Provide implementations that record values that were passed
* __Mocks__: Pre-prorammed to expect specific calls and parameter, and can throw exception when necessary

### Using unittest.Mock
* Provides many initialization parameters to control the mock objects behavior
* __spec__: specifies the interface to Mock
* __side_effect__: specifies a function that should be called
* __return_value__: specifies the return value when the Mock is called
* Provides many built-in functions for verify how it was used
* __assert_called__: Assert that mock was called
* __assert_called_once__: Assert that mock was called once
* __assert_called_with__: Assert that mock was called with the parameter
* __assert_called_once_with__: Assert that mock was called once with the parameter
* __assert_any_call__: Assert that mock was ever called with specified parameter
* __assert_not_called__ Assert that mock was not called
* Provides additional atributes for verification:
* __assert_has_calls__: Assert that mock was called with a list of calls
* __called__: A boolean indicator if the mock was ever called
* __call_count__: An integer representing the number of times that mock was called
* __call_args__: arguments that mock was last called with
* __call_args_list__: A list of arguments that were used for each call

## Section 7 - TDD Best Practices
* Doing the next simplest test case allow you to gradually increase the complexity of your code
* If you do complex test cases too quickly you will find yourself stuck writing a lot of functionality all at once
* Beyond slowing you down, this can also lead to bad design decisions
* Using descriptive names makes test clear and readable
* Unit test are the best documentation for how your code works
* Test suites should name the class or function under test and the test names should be describe the functionality being tested
* Mock out any slow collaborators with test doubles that are fast
* Use code coverage tools
* You should have a goal of 100% code coverage in functions with businnes logic in them (not simple getters and setters)
* Use a static code analysis tool like Pylint
* Focus on test the behavior rather than the implementation
