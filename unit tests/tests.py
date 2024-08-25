import unittest
import functions
import numpy as np

# Encoder tests
class TestEncoder(unittest.TestCase):
    def test_single_bit(self):
        self.assertEqual(0, functions.encoder(np.array([0])))
        self.assertEqual(1, functions.encoder(np.array([1])))

    def test_left_ceros(self):
        self.assertEqual(7, functions.encoder(np.array([1, 1, 1])))
        self.assertEqual(7, functions.encoder(np.array([0, 0, 1, 1, 1])))

    def test_other_cases(self):
        self.assertEqual(15, functions.encoder(np.array([1, 1, 1, 1])))
        self.assertEqual(0, functions.encoder(np.array([0, 0, 0, 0, 0])))
        self.assertEqual(13, functions.encoder(np.array([1, 1, 0, 1])))
        self.assertEqual(5, functions.encoder(np.array([0, 1, 0, 1])))
        self.assertEqual(10, functions.encoder(np.array([1, 0, 1, 0])))


if __name__ == '__main__':
    unittest.main()

