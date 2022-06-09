from unittest.mock import patch

import example.module1


class TestModule1:
    @staticmethod
    def test_sum():
        ret = example.module1.total([1, 2, 3, 4])
        assert ret == 10

    @staticmethod
    def test_mean_1():
        ret = example.module1.mean([1, 2, 3])
        assert ret == 2, "it's not 2"

    @staticmethod
    @patch("example.module2")
    def test_mean_2(mock_module2):
        def check_something():
            print("skip checking")

        mock_module2.check_something = check_something
        ret = example.module1.mean([1, 2, 3])
        assert ret == 2
