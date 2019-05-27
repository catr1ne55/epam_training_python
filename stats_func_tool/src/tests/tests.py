import unittest
import stats_func_tool.functions as stats


class TestStats(unittest.TestCase):

    def test_mean_positive(self):
        self.assertEqual(2.0, stats.mean([1, 2, 1, 5, 1]))

    def test_mean_negative(self):
        self.assertNotEqual(42, stats.mean([5, 4, 3, 2, 1]))

    def test_median_positive(self):
        self.assertEqual(2.0, stats.mean([1, 2, 1, 5, 1]))

    def test_median_negative(self):
        self.assertEqual(2.0, stats.mean([1, 2, 1, 5, 1]))

    def test_mode_positive(self):
        self.assertEqual([1], stats.mode([1, 2, 1, 5, 1]))

    def test_mode_negative(self):
        self.assertNotEqual([2], stats.mode([1, 2, 1, 5, 1]))

    def test_variance_positive(self):
        self.assertEqual(3.0, stats.variance([1, 2, 1, 5, 1]))

    def test_variance_negative(self):
        self.assertNotEqual(14, stats.variance([5, 4, 3, 2, 1]))

    def test_std_positive(self):
        self.assertEqual(1.5811388300841898, stats.std([5, 4, 3, 2, 1]))

    def test_std_negative(self):
        self.assertNotEqual(48, stats.std([5, 4, 3, 2, 1]))

    def test_data_range_positive(self):
        self.assertEqual(4, stats.data_range([1, 2, 1, 5, 1]))

    def test_data_range_negative(self):
        self.assertNotEqual(15, stats.mode([1, 2, 1, 5, 1]))

    def test_dot_positive(self):
        self.assertEqual(1, stats.dot([1, 0, 1, 1, 0], [0, 1, 0, 1, 0]))

    def test_dot_negative(self):
        self.assertNotEqual(15, stats.dot([1, 0, 4, 1, -9], [0, 1, 5, 1, 0]))

    # def test_cov_positive(self):
    #     self.assertEqual()
    #
    # def test_cov_negative(self):
    #     self.assertNotEqual()
    #
    # def test_corr_positive(self):
    #     self.assertEqual()
    #
    # def test_corr_negative(self):
    #     self.assertNotEqual()


if __name__ == '__main__':
    unittest.main()
