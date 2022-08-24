import unittest
from typing import List


def summary_ranges(nums: List[int]) -> List[str]:
    output = []

    if not nums:
        return output

    start = nums[0]
    end = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        if num - 1 == end:
            end = num
        else:
            if start != end:
                output.append('{}->{}'.format(start, end))
            else:
                output.append('{}'.format(start))
            start = num
            end = num

    if start != end:
        output.append('{}->{}'.format(start, end))
    else:
        output.append('{}'.format(start))

    return output


class SummaryRanges(unittest.TestCase):
    def test_01(self):
        self.assertEqual(['0->2', '4->5', '7'], summary_ranges([0, 1, 2, 4, 5, 7]))

    def test_02(self):
        self.assertEqual(['0', '2->4', '6', '8->9'], summary_ranges([0, 2, 3, 4, 6, 8, 9]))

    def test_03(self):
        self.assertEqual([], summary_ranges([]))
