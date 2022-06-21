import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/search-suggestions-system/
# There are two-way to solve this
def suggested_products(products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()  # O(n log n)

    res = []
    l, r = 0, len(products) - 1

    for i in range(len(searchWord)):  # O(m)
        c = searchWord[i]

        while l <= r and (len(products[l]) < i + 1 or products[l][i] != c):  # O(n)
            l += 1
        while l <= r and (len(products[r]) < i + 1 or products[r][i] != c):  # O(n)
            r -= 1

        res.append([])
        products_range = r - l
        for j in range(min(3, products_range + 1)):  # O(3)
            res[-1].append(products[j + l])

    return res


class SearchSuggestionsSystem(unittest.TestCase):
    def test_01(self):
        self.assertEqual([["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"],
                          ["mouse", "mousepad"], ["mouse", "mousepad"]],
                         suggested_products(products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
                                            searchWord="mouse"))

    def test_02(self):
        self.assertEqual([["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]],
                         suggested_products(products=["havana"], searchWord="havana"))

    def test_03(self):
        self.assertEqual([["baggage", "bags", "banner"], ["baggage", "bags", "banner"], ["baggage", "bags"], ["bags"]],
                         suggested_products(products=["bags", "baggage", "banner", "box", "cloths"], searchWord="bags"))
