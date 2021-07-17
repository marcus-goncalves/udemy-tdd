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