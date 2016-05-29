from .base import FunctionalTest

from wftda_importer.models import Player

class HomePageExists(FunctionalTest):
    '''Open up a page and it's got stats for Jill Nye across multiple available
bouts
    '''
    def test_multi_bout_stats_title(self):
        '''Make sure that the correct title is displayed'''
        url = [self.server_url,
               '/'
              ]
        self.browser.get(''.join(url))

        self.assertIn("Stats for Jill Nye", self.browser.title)

    def test_multi_bout_stats_shows_bouts(self):
        '''
        '''
        expected_name = "Holly Botts"
        p = Player()
        p.name = expected_name
        p.save()

        url = [self.server_url,
                '/%(id)'.format({"id":p.id})
              ]

        self.browser.get(''.join(url))

        self.assertIn("Stats for Holly Botts", self.browser.title)

        
