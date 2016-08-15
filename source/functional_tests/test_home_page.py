from .base import FunctionalTest

from wftda_importer.models import Player

class HomePageExists(FunctionalTest):
    """Open up a page and it's got stats for Jill Nye across multiple available
bouts
    """
    reset_sequences = True

    def setUp(self):
        self.url_prefix = '/display_stats'
        super().setUp()

    def test_landing_page_title(self):
        """Make sure that the correct title is displayed on the landing page"""
        expected_name = "Jill Nye"
        p = Player.objects.create(pk=1, name=expected_name)

        url = [self.server_url,
               self.url_prefix,
              ]
        self.browser.get(''.join(url))

        self.assertIn("Stats for {0}".format(expected_name), self.browser.title)

    def test_detail_page_title(self):
        """Ensure that the correct name shows up in the stat detail page for id=2"""
        expected_name = "Holly Botts"
        p1 = Player.objects.create()
        p2 = Player.objects.create(name=expected_name)

        url = [self.server_url,
                '{0}/{1}'.format(self.url_prefix, p2.id)
              ]

        self.browser.get(''.join(url))
        self.assertIn("Stats for {0}".format(expected_name), self.browser.title)

        
