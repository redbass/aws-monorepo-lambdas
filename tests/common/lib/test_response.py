import unittest

from lib.response import build_response


class ResponseTestCase(unittest.TestCase):
    def test_build_response_returns_correct_id(self):
        expected_id = 1
        self.assertEqual(
            {"lambda": expected_id},
            build_response(expected_id),
        )