import warnings

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django_webtest import WebTest

class ImporterPage(WebTest):
    """Open up a page and it's got an importer action that moves data into the
database"""

    def setUp(self):
        self.url_prefix = '/import'
        self.user = User.objects.create(username='foo')

        self.wftda_importer_page = self.app.get(reverse('wftda_importer'), 
                user=self.user)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.page_html = self.wftda_importer_page.html


        super().setUp()

    def test_landing_page_title(self):
        """Make sure that the correct title is displayed on the landing page"""
        expected_title = "WFTDA Statbook Importer"

        self.assertIn(expected_title, self.wftda_importer_page)

    def test_file_input_form_fields_exist(self):
        """Make sure that the page contains a file upload input"""
        form_tag = self.page_html.find('form', id='id_import_form')
        self.assertIsNotNone(form_tag)
        self.assertIsNotNone(form_tag.find('input', id='id_stat_book'))
        self.assertIsNotNone(form_tag.find('input', type='submit', 
            value='upload')) 

