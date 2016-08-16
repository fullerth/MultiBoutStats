from .base import FunctionalTest

class ImporterPage(FunctionalTest):
    """Open up a page and it's got an importer action that moves data into the
database"""

    def setUp(self):
        self.url_prefix = '/import'
        super().setUp()

    def test_landing_page_title(self):
        """Make sure that the correct title is displayed on the landing page"""
        expected_title = "WFTDA Statbook Importer"
        url = [self.server_url,
               self.url_prefix,
              ]
        self.browser.get(''.join(url))

        self.assertIn(expected_title, self.browser.title)

    def test_file_input_exists(self):
        """Make sure that the page contains a file upload input"""
        url = [self.server_url,
               self.url_prefix,
              ]
        self.browser.get(''.join(url))

        self.browser.find_element_by_id('id_file_input')
               



