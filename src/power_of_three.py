import unittest


# LeetCode link: https://leetcode.com/problems/power-of-three/
# TC: O(n)
# SC: O(1)
# We use loop until n greater than 1
def is_power_of_three(n: int) -> bool:
    while n % 3 == 0 and n > 1:
        n /= 3

    return n == 1


class PowerOfThree(unittest.TestCase):
    def test_01(self):
        self.assertEqual(True, is_power_of_three(27))

    def test_02(self):
        self.assertEqual(False, is_power_of_three(0))

    def test_03(self):
        self.assertEqual(True, is_power_of_three(9))

    def test_04(self):
        self.assertEqual(False, is_power_of_three(18))
