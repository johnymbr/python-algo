import unittest


# LeetCode link: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
# TC(O(min(m,n).(m+n))
# SC(O(min(m,n))
def gcd_of_strings(str1: str, str2: str) -> str:
    # first use the small string
    small_str = min(str1, str2)

    x = small_str
    divisor = 2
    while x:
        str1_inner = str1
        str2_inner = str2
        while str1_inner:
            str1_aux = str1_inner[:len(x)]
            if x == str1_aux:
                str1_inner = str1_inner[len(x):]
            else:
                break

        while str2_inner:
            str2_aux = str2_inner[:len(x)]
            if x == str2_aux:
                str2_inner = str2_inner[len(x):]
            else:
                break

        if not str1_inner and not str2_inner:
            return x

        x = small_str[:int(len(small_str) / divisor)]
        divisor += 1

    return ""


class GreatestCommonDivisorOfStrings(unittest.TestCase):
    def test_01(self):
        self.assertEqual("ABC", gcd_of_strings("ABCABC", "ABC"))

    def test_02(self):
        self.assertEqual("AB", gcd_of_strings("ABABAB", "ABAB"))

    def test_03(self):
        self.assertEqual("", gcd_of_strings("LEET", "CODE"))

    def test_04(self):
        self.assertEqual("A", gcd_of_strings("AAAA", "AAAAAAAAA"))
