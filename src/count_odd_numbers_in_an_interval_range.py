import unittest


# Leetcode link: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
# TC: O(1)
# SC: O(1)
def count_odds(low: int, high: int) -> int:
    count = 0

    if low % 2 != 0:
        count += 1
        low += 1

    if high % 2 != 0:
        count += 1
        high -= 1

    count += int((high - low) / 2)

    # count = int((high - low) / 2)
    #
    # if low % 2 != 0 or high % 2 != 0:
    #     count += 1
    #
    # return count

    return count


class CountOddNumbersInAnIntervalRange(unittest.TestCase):
    def test_01(self):
        self.assertEqual(3, count_odds(3, 7))

    def test_02(self):
        self.assertEqual(1, count_odds(8, 10))

    def test_03(self):
        self.assertEqual(86213013, count_odds(798273637, 970699661))
