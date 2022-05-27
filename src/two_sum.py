import unittest
from typing import List


# Leetcode Link: https://leetcode.com/problems/two-sum/
# It can be using brute force,
# or using a map that store the value and the index.
def two_sum(nums: List[int], target: int) -> List[int]:
    dict_tmp = {}
    for idx in range(len(nums)):
        diff = target - nums[idx]
        if dict_tmp.get(diff) is not None:
            return [dict_tmp.get(diff), idx]

        dict_tmp[nums[idx]] = idx


class TwoSumTest(unittest.TestCase):
    def test_01(self):
        result = two_sum(nums=[2, 7, 11, 15], target=9)
        print(result)
        self.assertEqual(result, [0, 1])


if __name__ == "__main__":
    unittest.main()
