import unittest


# Leetcode link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# TC: O(n.m)
# SC: O(1)
def str_str(haystack: str, needle: str) -> int:
    first_c = -1
    h_len = len(haystack)
    n_len = len(needle)
    if h_len < n_len:
        return first_c

    for i in range(h_len):
        same = False
        if haystack[i] == needle[0]:
            if h_len - i >= n_len:
                first_c = i
                i_aux = i
                same = True
                for j in range(n_len):
                    if haystack[i_aux] == needle[j]:
                        i_aux += 1
                    else:
                        same = False
                        break

                if not same:
                    first_c = -1
        else:
            first_c = -1

        if same:
            break

    return first_c


class FindIndexFirstOccurrenceString(unittest.TestCase):
    def test_01(self):
        self.assertEqual(0, str_str("sadbutsad", "sad"))

    def test_02(self):
        self.assertEqual(-1, str_str("leetcode", "leeto"))

    def test_03(self):
        self.assertEqual(-1, str_str("mississippi", "issipi"))
