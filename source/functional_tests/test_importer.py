from .base import FunctionalTest

class ImporterPage(FunctionalTest):
    """Open up a page and it's got an importer action that moves data into the
database"""

    def setUp(self):
        super().setUp()

    def test_landing_page_title(self):
        """Make sure that the correct title is displayed on the landing page"""
        expected_title = "WFTDA Statbook Importer"
        url = [self.server_url,
               '/import',
              ]
        self.browser.get(''.join(url))

        self.assertIn(expected_title, self.browser.title)


