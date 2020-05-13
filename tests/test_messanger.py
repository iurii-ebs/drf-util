from django.test import TestCase

from drf_util.messanger import send_text_message, send_html_message


class DecoratorsTests(TestCase):

    def test_await_process_decorator(self):
        result = send_text_message("test@gmail.com", "Title test", "Text test")
        print(result)
        # self.assertEqual(True, result)
