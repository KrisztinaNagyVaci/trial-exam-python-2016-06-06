# Write unittests for this function:
import unittest


def greeter(name):
  if len(name):
    return 'Hello, ' + name + '!'
  else:
    return 'Hello, Mr Nobody!'

class MyTest(unittest.TestCase):
    def test_string_input_was_given(self):
        self.assertEqual(greeter('Malinda'), 'Hello, Malinda!')

    def test_no_input_was_given(self):
        self.assertEqual(greeter(''), 'Hello, Mr Nobody!')

    # def test_integer_input_was_given(self):
        # self.assertNotEqual(greeter(3), 'Hello, 3!')


if __name__ == '__main__':
    unittest.main()
