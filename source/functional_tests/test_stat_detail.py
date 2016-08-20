from .base import FunctionalTest

from wftda_importer.models import Player, Jam, PlayerToJam

class StatDetailPage(FunctionalTest):
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

    def test_jams_played_displayed_correctly(self):
        """Ensure the number of jams played is displayed properly"""
        expected_jams = 16
        total_jams = 20
        p = Player.objects.create() 
        
        for i in range(0, total_jams):
            j = Jam.objects.create()
            j.save()
            if(i < expected_jams):
                PlayerToJam.objects.create(player=p, jam=j)
        
        url = [self.server_url,
                '{0}/{1}'.format(self.url_prefix, p.id)
              ]

        self.browser.get(''.join(url))
        expected_strs = ['jams: {0}'.format(expected_jams),
                ]
        for expected in expected_strs:
            self.assertIn(expected,
                    self.browser.page_source, 
                    msg="'{0}' not found on page".format(expected)
            )

    def test_total_jams_displayed(self):
        """Ensure the total number of jams is displayed on the page"""
        expected_jams = 20
        p = Player.objects.create()
        
        for i in range(0, expected_jams):
            Jam.objects.create()

        url = [self.server_url,
                '{0}/{1}'.format(self.url_prefix, p.id)
              ]

        self.browser.get(''.join(url))

        total_jams = self.browser.find_element_by_id('id_total_jams')

        self.assertIn(str(expected_jams), total_jams.get_attribute('innerHTML'), 
                msg="Total number of jams not found on page")

    def test_positions_displayed_correctly(self):
        """Ensure the number of jams played as a blocker are displayed"""
        expected_jammer = 8
        expected_blocker = 5
        expected_pivot = 3
        total_jams = expected_jammer + expected_blocker + expected_pivot 
        p = Player.objects.create()

        for i in range(0, total_jams):
            j = Jam.objects.create()
            if(i < expected_jammer):
                PlayerToJam.objects.create(player=p, jam=j,
                        position=PlayerToJam.JAMMER)
            elif(i < (expected_jammer + expected_blocker)):
                PlayerToJam.objects.create(player=p, jam=j,
                        position=PlayerToJam.BLOCKER)
            elif(i < (expected_jammer + expected_blocker + expected_pivot)):
                PlayerToJam.objects.create(player=p, jam=j,
                        position=PlayerToJam.PIVOT)

        url = [self.server_url,
                '{0}/{1}'.format(self.url_prefix, p.id)
              ]

        self.browser.get(''.join(url))

        jammer_jams = self.browser.find_element_by_id('id_jammer_jams')
        blocker_jams = self.browser.find_element_by_id('id_blocker_jams')
        pivot_jams = self.browser.find_element_by_id('id_pivot_jams')

        self.assertIn(str(expected_jammer), 
                jammer_jams.get_attribute('innerHTML'),
                msg="Number of Jams as blocker not found in id_jammer_jams")
        self.assertIn(str(expected_blocker), 
                blocker_jams.get_attribute('innerHTML'),
                msg="Number of Jams as blocker not found in id_blocker_jams")
        self.assertIn(str(expected_pivot), 
                pivot_jams.get_attribute('innerHTML'),
                msg="Number of Jams as blocker not found in id_pivot_jams")

