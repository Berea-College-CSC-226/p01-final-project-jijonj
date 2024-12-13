################################################################################
##  Author: Julio Jijon
##  Username: jijonj
##  Purpose: to test my partner's function
################################################################################

from inspect import getframeinfo, stack

import chapter_6_1_function


def unitTest(pass_test):
    """ function that prints out the result of a test
        :param pass_test: a boolean representing the test
        :return: None

    """

    caller = getframeinfo(stack()[1][0])

    if pass_test:
        message = f"Test at line {caller.lineno} ok."
    else:
        message = f"Test at line {caller.lineno} failed."

    print(message)

def chapter6_function_test():
    """ function that uses the test suite to ensure that function works
        :return: None

    """

    # run tests on with some pass in values
    print("Test suite is now running....")

    unitTest(check("B") == True)
    unitTest(check("C") == False)
    unitTest(check("f") == False)
    unitTest(check("b") == True)
    unitTest(check("z")== False)
    unitTest(check(4) == False)
    unitTest(check(9.0) == False)


def main():
    """main function that calls the test suite function"""

    chapter6_function_test() # call test function

if __name__ == "__main__":
    main() # call main function