from django.test import TestCase

from wftda_importer.models import Player

class WftdaImporterTests(TestCase):
    def setUp(self):
        pass

    def test_empty_failed_test(self):
        self.assertEqual(0, 1)
