from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django_webtest import WebTest

class ImporterPage(WebTest):
    """Open up a page and it's got an importer action that moves data into the
database"""

    def setUp(self):
        self.url_prefix = '/import'
        self.user = User.objects.create(username='foo')
        super().setUp()

    def test_landing_page_title(self):
        """Make sure that the correct title is displayed on the landing page"""
        expected_title = "WFTDA Statbook Importer"
        wftda_importer_page = self.app.get(reverse('wftda_importer'), 
                user=self.user)

        self.assertIn(expected_title, wftda_importer_page)

    def test_file_input_exists(self):
        """Make sure that the page contains a file upload input"""
        wftda_importer = self.app.get(reverse('wftda_importer'),
                user=self.user)

        self.assertIn('id_file_input', wftda_importer)
               
