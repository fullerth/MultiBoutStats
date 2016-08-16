from django.core.urlresolvers import reverse

from django.test import TestCase
from django.test.client import Client

class ImporterPageTest(TestCase):
    """Unit tests for Importer view"""

    def setUp(self):
        self.test_url_name = 'wftda_importer'

    def test_page_renders_with_correct_template(self):
        """Ensure the correct template is used to display the importer"""
        c = Client()
        response = c.get(reverse(self.test_url_name))
        self.assertTemplateUsed(response, 'wftda_importer/import.html')


