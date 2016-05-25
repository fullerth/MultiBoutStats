from django.test import TestCase

class WftdaImporterTests(TestCase):
    def setUp(self):
        pass

    def test_empty_failed_test(self):
        self.assertEqual(0, 1)
