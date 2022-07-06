import unittest


# LeetCode link: https://leetcode.com/problems/fibonacci-number/
# Time complexity: O(n)
# Space complexity: O(n) because we are using recursion.
def fib(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


# Time complexity: O(n)
# Space complexity: O(1)
# In this solution, we didn't use recursion, only an array with two position that
# contains the last two values.
def fib_ii(n: int) -> int:
    prev = [0, 1]
    if n == 0:
        return prev[0]
    if n == 1:
        return prev[1]

    for i in range(2, n):
        aux = prev[0] + prev[1]
        prev[0], prev[1] = prev[1], aux

    return prev[0] + prev[1]


class FibonacciNumber(unittest.TestCase):
    def test_01(self):
        self.assertEqual(1, fib(2))

    def test_02(self):
        self.assertEqual(2, fib(3))

    def test_03(self):
        self.assertEqual(3, fib(4))

    def test_04(self):
        self.assertEqual(1, fib_ii(2))

    def test_05(self):
        self.assertEqual(2, fib_ii(3))

    def test_06(self):
        self.assertEqual(3, fib_ii(4))
