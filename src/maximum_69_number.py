import unittest


def maximum_69_number(num: int) -> int:
    aux = num

    mult = 1
    sum = 0
    while aux > 0:
        rest = aux % 10
        if 9 - rest > 0:
           sum = max(sum, (9 - rest) * mult)

        mult *= 10
        aux = int(aux / 10)

    return num + sum


class Maximum69Number(unittest.TestCase):
    def test_01(self):
        self.assertEqual(9969, maximum_69_number(9669))

    def test_02(self):
        self.assertEqual(9999, maximum_69_number(9996))

    def test_03(self):
        self.assertEqual(9999, maximum_69_number(9999))
