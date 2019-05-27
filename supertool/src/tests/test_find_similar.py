import unittest
import supertool.find_similar as finder


class TestSimilarFilesFinder(unittest.TestCase):
    """
    Tests for the find_similar.py

    """

    def test_wrong_input_data(self):
        with self.assertRaises(Exception) as e:
            finder.find_similar('strange_directory')
        self.assertEqual("This directory doesn't exist. Please try again with existing directory!", e.exception.args[0])

    def test_with_good_input(self):
        self.assertDictEqual(finder.find_similar('/home/catr1ne55/PycharmProjects/supertool/src/tests/direct'),
                             {
                                 'da39a3ee5e6b4b0d3255bfef95601890afd80709': ['/home/catr1ne55/PycharmProjects/supertool/src/tests/direct/2'],
                                 'f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0': [
                                     '/home/catr1ne55/PycharmProjects/supertool/src/tests/direct/1',
                                     '/home/catr1ne55/PycharmProjects/supertool/src/tests/direct/3']
                                 })

    def test_empty_directory(self):
        self.assertDictEqual(finder.find_similar('/home/catr1ne55/PycharmProjects/supertool/src/tests/dir1'), {})


if __name__ == '__main__':
    unittest.main()
