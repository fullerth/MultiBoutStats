from .base import FunctionalTest

from wftda_importer.models import Player, Jam, PlayerToJam

class StatDetailPage(FunctionalTest):
    """Open up a page and it's got stats for Jill Nye across multiple available
bouts
    """
    reset_sequences = True

    def setUp(self):
        self.url_prefix = '/display_stats'
        self.url = [self.server_url,
                    self.url_prefix,
                   ]
        self.expected_players = [
            {
                "player":{"name":"Jill Nye", 'pk':1},
                "positions":{"blocker":16, "pivot":0, "jammer":0},
            }, 
            {
                "player":{"name":"Cassie Beck", "pk":2},
                "positions":{"blocker":5,  "pivot":3, "jammer":2},
            },
        ]

        #This should eventually be calculated from expected_players dict, but
        #for now is sufficient to be greater than the most number of played jams
        self.total_jams = 20

        self.created_players = []
        self.expected_elements = []
        self.created_jams = []
        self.created_playertojams = []

        self.__create_jams(self.total_jams)
        self.__create_players(new_players=self.expected_players)
        super().setUp()

    def __create_players(self, new_players=[{"name":"Default",
                                           "pk":None}]
                            ):
        """players is a list of dicts to be passed to Player model as kwargs"""
        for current_player in new_players:
            player = Player.objects.create(**current_player['player'])

            self.created_players.append(player)
            self.__put_player_in_jams(player=player, 
                    positions=current_player['positions'])

    def __create_jams(self, number):
        for i in range(0, number):
            self.created_jams.append(Jam.objects.create())

    def __put_player_in_jams(self, player, positions):
        """Pass a player and a dictionary of the positions they should play"""
        blocker = positions['blocker']
        pivot = positions['pivot']
        jammer = positions['jammer']
        for i in range(0, blocker+pivot+jammer):
            position = None
            if(i < blocker):
                position = PlayerToJam.BLOCKER
            elif(i < blocker+pivot):
                position = PlayerToJam.PIVOT
            elif(i < blocker+pivot+jammer):
                position = PlayerToJam.JAMMER
            
            self.created_playertojams.append(PlayerToJam.objects.create(
                player=player, jam=self.created_jams[i], position=position))

    def __verify_expected_elements(self):
        for test in self.expected_elements:
            if 'message' not in test:
                test['message'] = None
            if 'name' not in test:
                test['name'] = None
            with self.subTest(msg=test['name']):
                self.assertIn(test['string'], test['location'], msg=test['message'])


    def test_landing_page_title(self):
        """Make sure that the correct title is displayed on the landing page"""
        expected_name = self.created_players[0].name
        self.browser.get(''.join(self.url))

        self.expected_elements.append({
            "name":"Landing Page Title",
            "string":"Stats for {0}".format(expected_name), 
            "location":self.browser.title,
            "message":"{0} not found in browser title".format(expected_name),
        })

        self.__verify_expected_elements()

    def test_detail_page_elements(self):
        """Ensure that the correct name shows up in the stat detail page for id=2"""
        p2 = self.created_players[1]

        self.url.append('/{0}'.format(p2.id))

        self.browser.get(''.join(self.url))

        self.expected_elements.append({
            "name":"Detail Page Title",
            "string":"Stats for {0}".format(p2.name),
            "location":self.browser.title,
            "message":"{0} not found in browser title for player id {1}".format(
                p2.name, p2.id)
        })

        self.__verify_expected_elements()

    def test_jams_played_displayed_correctly(self):
        """Ensure the number of jams played is displayed properly"""
        p = self.created_players[0]
        position = self.expected_players[0]['positions']
        expected_jams = position['blocker']+position['pivot']+position['jammer']

        
        self.url.append('/{0}'.format(p.id))
        self.browser.get(''.join(self.url))

        expected_string = 'jams: {0}'.format(expected_jams)

        self.expected_elements.append({
            "name":"Jams Played Display",
            "string":expected_string,
            "location":self.browser.find_element_by_id(
                'id_played_jams').get_attribute('innerHTML'),
            "message":"{0} not found in id_played_jams".format(expected_string), 
        })

        self.__verify_expected_elements()

    def test_total_jams_displayed(self):
        """Ensure the total number of jams is displayed on the page"""
        p = self.created_players[0]
        self.url.append('/{0}'.format(p.id))

        self.browser.get(''.join(self.url))

        total_jams = self.browser.find_element_by_id('id_total_jams')

        self.assertIn(str(self.total_jams), total_jams.get_attribute('innerHTML'), 
                msg="Total number of jams not found on page")

    def test_positions_displayed_correctly(self):
        """Ensure the number of jams played as a blocker are displayed"""
        p = self.created_players[1]
        expected_blocker = self.expected_players[1]['positions']['blocker']
        expected_pivot = self.expected_players[1]['positions']['pivot']
        expected_jammer = self.expected_players[1]['positions']['jammer']

        self.url.append('/{0}'.format(p.id))

        self.browser.get(''.join(self.url))

        jammer_jams = self.browser.find_element_by_id('id_jammer_jams')
        blocker_jams = self.browser.find_element_by_id('id_blocker_jams')
        pivot_jams = self.browser.find_element_by_id('id_pivot_jams')

        import pdb; pdb.set_trace()

        self.assertIn(str(expected_jammer), 
                jammer_jams.get_attribute('innerHTML'),
                msg="Number of Jams as blocker not found in id_jammer_jams")
        self.assertIn(str(expected_blocker), 
                blocker_jams.get_attribute('innerHTML'),
                msg="Number of Jams as blocker not found in id_blocker_jams")
        self.assertIn(str(expected_pivot), 
                pivot_jams.get_attribute('innerHTML'),
                msg="Number of Jams as blocker not found in id_pivot_jams")

