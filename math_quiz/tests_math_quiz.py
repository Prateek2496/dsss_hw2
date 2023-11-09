import unittest
from math_quiz import randomIntegerGenerator, randomOperationSelector, performMathOperation

class TestMathGame(unittest.TestCase):

    def test_randomIntegerGenerator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomIntegerGenerator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
            
    def test_randomOperationSelector(self):
        # Test if the random operator returned is part of the list of allowed operators
        OpearatorList = ['+', '-', '*']
        for _ in range(1000):
            randomOperator = randomOperationSelector()
            self.assertTrue(randomOperator in OpearatorList)
            
    def test_performMathOperation(self):
            test_cases = [
                (5, 2, '+', '5.0 + 2.0', 7.0),
                (10, 3, '-', '10.0 - 3.0', 7.0),
                (4, 2, '*', '4.0 * 2.0', 8.0),
                (7.5, 3, '+', '7.5 + 3.0', 10.5),
                (12, 4, '*', '12.0 * 4.0', 48.0),
                (-5, 3, '-', '-5.0 - 3.0', -8.0),
                ('8', '2', '+', '8.0 + 2.0', 10.0),
                ('5.5', '1.5', '*', '5.5 * 1.5', 8.25),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                p, a = performMathOperation(num1, num2, operator)
                self.assertTrue(p == expected_problem and a == expected_answer)

if __name__ == "__main__":
    unittest.main()
