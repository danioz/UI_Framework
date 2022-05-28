import unittest
from unittest import TestLoader
import concurrent.futures
from tests.suite.testCases import Test_Smoke, Test_Error_Messages, Test_Login

testCases = (Test_Login, Test_Smoke, Test_Error_Messages)


def run(testCase):
    unittest.TextTestRunner(verbosity=2).run(testCase)


def loadedTests():
    loadedTestCases = [unittest.TestLoader().loadTestsFromTestCase(test)
                       for test in testCases]
    return loadedTestCases


def executeParallel(tests):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(run, tests)


if __name__ == '__main__':
    executeParallel(loadedTests())
