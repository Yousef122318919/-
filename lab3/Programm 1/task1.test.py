import unittest
import task1

class TestTask1(unittest.TestCase):
    def test_no_emotions(self):
        data = 'nobody here'
        result = 0
        self.assertEqual(result, task1.solve(data))

    def test_breaked_emotions(self):
        data = 'Hello ;< ) :<0 ; <) ;<here)'
        result = 0
        self.assertEqual(result, task1.solve(data))

    def test_one_emotion(self):
        data = ':-P'
        result = 1
        self.assertEqual(result, task1.solve(data))

    def test_many_emotions(self):
        data = ':-P:-P:-P:-P:-P:-P'
        result = 6
        self.assertEqual(result, task1.solve(data))

    def test_emotions_with_splits(self):
        data = '[]:-P hi ;;:-P))      :-P:-P:-P-<)'
        result = 5
        self.assertEqual(result, task1.solve(data))

if __name__ == '__main__':
    unittest.main()