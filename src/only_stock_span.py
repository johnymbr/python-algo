import unittest


# Leetcode link: https://leetcode.com/problems/online-stock-span/description/
# TC: O(1)
# SC: O(n)
# We use a strategy named monotonically stack, which store the price and counter that store how many days consecutives
# this price is greater than.
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        c = 1
        while self.stack and self.stack[-1][0] <= price:
            c += self.stack.pop()[1]

        self.stack.append((price, c))

        return c


class OnlyStockSpan(unittest.TestCase):

    def test_01(self):
        obj = StockSpanner()
        self.assertEqual(1, obj.next(100))
        self.assertEqual(1, obj.next(80))
        self.assertEqual(1, obj.next(60))
        self.assertEqual(2, obj.next(70))
        self.assertEqual(1, obj.next(60))
        self.assertEqual(4, obj.next(75))
        self.assertEqual(6, obj.next(85))
