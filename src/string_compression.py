import unittest
from typing import List


# Leetcode link: https://leetcode.com/problems/string-compression/description/
# TC: O(n)
# SC: O(1)
def compress(chars: List[str]) -> int:
    def change(c, first_idx, count) -> int:
        chars[first_idx] = c
        first_idx += 1
        if count == 1:
            return 1
        str_repr = str(count)
        chars[first_idx:first_idx+len(str_repr)] = list(str_repr)
        return len(str_repr) + 1

    n = len(chars)
    if n == 1:
        return 1

    size = 0
    previous = chars[0]
    first_idx = 0
    count = 0
    for i in range(len(chars)):
        curr = chars[i]
        if previous == curr:
            count += 1
        else:
            # gravar no chars
            size += change(previous, first_idx, count)
            count = 1
            first_idx = size

        previous = curr

    size += change(previous, first_idx, count)

    return size


class StringCompression(unittest.TestCase):
    def test_01(self):
        self.assertEqual(6, compress(["a", "a", "b", "b", "c", "c", "c"]))

    def test_02(self):
        self.assertEqual(1, compress(["a"]))

    def test_03(self):
        self.assertEqual(4, compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))

    def test_04(self):
        self.assertEqual(6, compress(["a", "a", "a", "b", "b", "a", "a"]))
