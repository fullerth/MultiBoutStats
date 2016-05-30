from .base import FunctionalTest

from wftda_importer.models import Player

class HomePageExists(FunctionalTest):
    """Open up a page and it's got stats for Jill Nye across multiple available
bouts
    """
    def setUp(self):
        self.url_prefix = '/display_stats/'
        super().setUp()

    def test_multi_bout_stats_title(self):
        """Make sure that the correct title is displayed"""
        url = [self.server_url,
               self.url_prefix,
              ]
        self.browser.get(''.join(url))

        self.assertIn("Stats for Jill Nye", self.browser.title)

    def test_multi_bout_stats_shows_bouts(self):
        """Ensure that the correct name shows up in the stat detail page"""
        expected_name = "Holly Botts"
        p = Player()
        p.name = expected_name
        p.save()

        url = [self.server_url,
                '{0}/{1}/'.format(self.url_prefix, p.id)
              ]

        self.browser.get(''.join(url))

        self.assertIn("Stats for Holly Botts", self.browser.title)

        
