import unittest


# LeetCode link: https://leetcode.com/problems/isomorphic-strings/
# TC: O(n)
# SC: O(1) - once the maximum length of maps as ASCII characters.
def is_isomorphic(s: str, t: str) -> bool:
    s_map, t_map = {}, {}

    for i in range(len(s)):
        sc = s[i]
        tc = t[i]
        if not s_map.get(sc) and not t_map.get(tc):
            s_map[sc] = tc
            t_map[tc] = sc
        else:
            s_aux = s_map.get(sc)
            t_aux = t_map.get(tc)

            if s_aux != tc and t_aux != sc:
                return False

    return True


class IsomorphicStrings(unittest.TestCase):
    def test_01(self):
        self.assertEqual(True, is_isomorphic('egg', 'add'))

    def test_02(self):
        self.assertEqual(False, is_isomorphic('foo', 'bar'))

    def test_03(self):
        self.assertEqual(True, is_isomorphic('paper', 'title'))

    def test_04(self):
        self.assertEqual(True, is_isomorphic('13', '42'))
