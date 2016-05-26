from .base import FunctionalTest

class HomePageExists(FunctionalTest):
    '''Open up a page and it's got stats for Jill Nye across multiple available
bouts
    '''
    def test_multi_bout_stats_title(self):
        '''Make sure that a title is displayed to the user'''
        url = [self.server_url,
               '/'
              ]
        self.browser.get(''.join(url))

        self.assertIn("Stats for Jill Nye", self.browser.title)
