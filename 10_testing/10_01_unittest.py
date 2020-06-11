'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''
import unittest

def divide(x, y):
    return int(x/y)

class TestExample(unittest.TestCase):
    def test_divide(self):
        x = 10
        y = 5
        self.assertEqual(2, divide(x, y))

    def test_divide2by3(self):
        x = 6
        y = 4
        self.assertEqual(1.5, divide(x, y))


        # try:
        #     if x == y:
        #         result = divide(x, y)
        #         self.assertEqual(result, 1)
        #     if not x == y:
        #         result = divide(x, y)
        #         self.assertNotEqual(result, 1)
        # except ZeroDivisionError as zde:
        #     print(zde)

