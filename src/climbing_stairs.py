import unittest


# Leetcode link: https://leetcode.com/problems/climbing-stairs/description/
# TC: O(n)
# SC: 1
# It used DP to solve this problem.
# I used two variables that stores the last two values,
# and on each loop, it is stored on variable one the value of one plus two
# and in the two it is stored the old value of one.
def climb_stairs(n: int) -> int:
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one


class ClimbingStairs(unittest.TestCase):
    def test_01(self):
        self.assertEqual(2, climb_stairs(2))

    def test_02(self):
        self.assertEqual(3, climb_stairs(3))

    def test_03(self):
        self.assertEqual(8, climb_stairs(5))
