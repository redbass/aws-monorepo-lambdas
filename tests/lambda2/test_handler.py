from lambda2.handler import handler
from unittest import TestCase, mock


class HandlerTestCase(TestCase):
    @mock.patch("lambda2.handler.build_response")
    def test_handler_return_default_content(self, mock_build_response):
        response = handler(mock.ANY, mock.ANY)

        mock_build_response.assert_called_once_with(2)