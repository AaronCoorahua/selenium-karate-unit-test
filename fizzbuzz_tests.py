import unittest

class FizzBuzzTests(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "fizz")
        self.assertEqual(fizzbuzz(6), "fizz")
        self.assertEqual(fizzbuzz(9), "fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")
        self.assertEqual(fizzbuzz(10), "buzz")
        self.assertEqual(fizzbuzz(20), "buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "fizzbuzz")
        self.assertEqual(fizzbuzz(30), "fizzbuzz")
        self.assertEqual(fizzbuzz(45), "fizzbuzz")

    def test_other_numbers(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(7), "7")

if __name__ == '__main__':
    unittest.main()
