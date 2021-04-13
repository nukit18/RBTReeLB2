import unittest
from random import randint

from RBTree import RBTree


def get_sort(arr):
    rb = RBTree()
    for e in arr:
        rb.insert(e)
    rb.getsorted(rb.root)
    result = rb.result
    return result


class TestMethods(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(get_sort([]), [])

    def test_one_element(self):
        self.assertEqual(get_sort(["a"]), ["a"])

    def test_simple_strings(self):
        self.assertEqual(get_sort(["b", "a", "c"]), ["a", "b", "c"])

    def test_simple_strings_different_cases(self):
        self.assertEqual(get_sort(["A", "a", "B", "b"]), ["A", "B", "a", "b"])

    def test_simple_strings_special_character(self):
        self.assertEqual(get_sort(["a", "A", "]", "B"]), ["A", "B", "]", "a"])

    def test_strings(self):
        self.assertEqual(get_sort("AdhjdfvvBnfhdkG361nTvf83bf47..39493.f;@]".split()),
                         sorted("AdhjdfvvBnfhdkG361nTvf83bf47..39493.f;@]".split()))

    def test_long_strings(self):
        self.assertEqual(get_sort(["aaa", "aba", "bba", "aab", "abb"]), ["aaa", "aab", "aba", "abb", "bba"])

    def test_long_strings_different_cases(self):
        self.assertEqual(get_sort(["bbF", "Aaa", "ABA", "Cba", "Bab", "bba"]),
                         ["ABA", "Aaa", "Bab", "Cba", "bbF", "bba"])

    def test_long_strings_special_character(self):
        self.assertEqual(get_sort(["!", "a!", "@a!"]), ["!", "@a!", "a!"])

    def test_long_strings_special_character_different_cases(self):
        self.assertEqual(get_sort(["A!", "a!", "@a!"]), ["@a!", "A!", "a!"])

    def test_same_elements(self):
        self.assertEqual(get_sort(["b", "b", "b"]), ["b", "b", "b"])

    def test_same_elements_with_one_different(self):
        self.assertEqual(get_sort(["b", "a", "b"]), ["a", "b", "b"])

    def test_simple_numbers(self):
        self.assertEqual(get_sort([5, 7, 1, 3]), [1, 3, 5, 7])

    def test_more_numbers(self):
        array = []
        for i in range(1000):
            array.append(randint(0, 100000))
        self.assertEqual(get_sort(array),
                         sorted(array))


if __name__ == '__main__':
    unittest.main()
