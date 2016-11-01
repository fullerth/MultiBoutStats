from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.test import TestCase
from django.test.client import Client

class ImporterPageTest(TestCase):
    """Unit tests for Importer view"""

    def setUp(self):
        self.user = User.objects.create(username='foo')
        self.test_url_name = 'wftda_importer'

    def test_page_renders_with_correct_template(self):
        """Ensure the correct template is used to display the importer"""
        c = Client()
        c.force_login(self.user)
        response = c.get(reverse(self.test_url_name), user=self.user)
        self.assertTemplateUsed(response, 'wftda_importer/import.html')

    def test_page_requires_login(self):
        """Ensure the importer page redirects to the login"""
        c = Client()
        response = c.get(reverse(self.test_url_name))
        
        self.assertRedirects(response, '{0}?next={1}'.format(
            reverse('login'), reverse(self.test_url_name)))


