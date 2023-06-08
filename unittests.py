# Худяков Иван Андреевич 44-22-112 вариант 26


import unittest
from calculate import calculate
import numpy as np


class UnitTest1(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(
            np.allclose(
                np.array(calculate(0.2, 0.4, 10, 20)),
                np.array([
                    0.6458829262950192,
                    1.3754361845033998,
                    148.44684501466074,
                    22026.466248806
                ])
            )
        )

    def test_nan(self):
        self.assertFalse(bool(calculate(-1)[0]))
        self.assertFalse(bool(calculate("НЕ ЧИСЛО")[0]))
        self.assertFalse(bool(calculate(None)[0]))


if __name__ == "__main__":
    unittest.main()