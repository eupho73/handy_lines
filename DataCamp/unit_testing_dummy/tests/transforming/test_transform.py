import pytest
from transforming.transform import str_of_int_to_list

class TestConcatListInt(object):
    def test_concat_list_int_normal(self):
        actual = str_of_int_to_list("[1, 2, 3, 4]")
        expected = [1, 2, 3, 4]
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)