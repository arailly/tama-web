from unittest import TestCase
import handlers.passages as handler


class Test(TestCase):
    def test_index(self):
        res = handler.index('../data/passages')
        self.assertIn('sample.csv', res['files'])
