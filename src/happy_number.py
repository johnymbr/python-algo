import unittest


# LeetCode link: https://leetcode.com/problems/happy-number/
# TC O(log n)
# SC O(n)
def is_happy(n: int) -> bool:
    visited = set()
    while n != 1:
        local_sum = 0
        while n > 0:
            local_sum += (n % 10) ** 2
            n = n // 10

        if local_sum in visited:
            break

        visited.add(local_sum)
        n = local_sum

    return True if n == 1 else False


class HappyNumber(unittest.TestCase):
    def test_01(self):
        self.assertEqual(True, is_happy(7))

    def test_02(self):
        self.assertEqual(False, is_happy(2))
