'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''
import unittest

def divide(x, y):
    return x / y

class TestExample(unittest.TestCase):
    def test_divide(self):
        x = int(input("Please enter a number: "))
        y = int(input("Please enter another number: "))
        try:
            if x == y:
                result = divide(x, y)
                self.assertEqual(result, 1)
            if not x == y:
                result = divide(x, y)
                self.assertNotEqual(result, 1)
        except ZeroDivisionError as zde:
            print(zde)

# need test that does not pass