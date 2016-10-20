from .base import FunctionalTest

from wftda_importer import factories
from wftda_importer.models import Bout, PlayerToJam, Jam

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
        
        self.created_bouts = factories.CompleteBoutFactory.create_batch(2)
        self.expected_elements = []

        super().setUp()

    def __verify_expected_elements(self):
        for test in self.expected_elements:
            if 'message' not in test:
                test['message'] = None
            if 'name' not in test:
                test['name'] = None
            with self.subTest(msg=test['name']):
                self.assertIn(test['string'], test['location'], msg=test['message'])

    def test_detail_page_elements(self):
        """Ensure that the correct element values show up in the stat detail page for id=2"""
        p2 = self.created_bouts[1].home_roster.players.all()[0]

        total_jams_available_p2 = Jam.objects.filter(
                bout__home_roster__players=p2).count()

        position = {
            "blocker":PlayerToJam.objects.filter(
                player=p2, position=PlayerToJam.BLOCKER).count(), 
            "pivot":PlayerToJam.objects.filter(
                player=p2, position=PlayerToJam.PIVOT).count(), 
            "jammer":PlayerToJam.objects.filter(
                player=p2, position=PlayerToJam.JAMMER).count()
        }

        status = {
            "lead":PlayerToJam.objects.filter(
                player=p2, lead_flag=True).count()
        }

        expected_blocker = "blocker jams: {0}".format(position['blocker'])
        expected_pivot = "pivot jams: {0}".format(position['pivot'])
        expected_jammer = "jammer jams: {0}".format(position['jammer'])
        expected_lead_jammer = "lead jammer: {0}".format(status['lead'])

        self.url.append('/{0}'.format(p2.id))
        self.browser.get(''.join(self.url))

        expected_name = p2.name
        expected_title_string = "Stats for {0}".format(expected_name)

        expected_bouts = "bouts: {0}".format(Bout.objects.filter(
            home_roster__players=p2).count())

        self.expected_elements.append({
            "name":"Detail Page Title",
            "string":expected_title_string,
            "location":self.browser.title,
            "message":
                "'{0}' not found in browser title for player id {1}".format(
                expected_title_string, p2.id)
        })

        expected_jams_played = "jams: {0}".format(
            position['blocker']+position['pivot']+position['jammer'])
        self.expected_elements.append({
            "name":"Jams Played Display",
            "string":expected_jams_played,
            "location":self.browser.find_element_by_id(
                'id_played_jams').get_attribute('innerHTML'),
            "message":"'{0}' not found in id_played_jams".format(
                expected_jams_played), 
        })

        total_jams_available = "total jams available: {0}".format(
                total_jams_available_p2)
        self.expected_elements.append({
            "name":"Total Jams Available to Player Display",
            "string":total_jams_available,
            "location":self.browser.find_element_by_id(
                'id_total_jams_available').get_attribute('innerHTML'),
            "message":"'{0}' not found in id_total_jams_available".format(
                total_jams_available)
        })

        self.expected_elements.append({
            "name":"Jams as Jammer Display",
            "string":expected_jammer,
            "location":self.browser.find_element_by_id(
                'id_jammer_jams').get_attribute('innerHTML'),
            "message":"'{0}' not found in id_jammer_jams".format(
                expected_jammer)
        })
        
        self.expected_elements.append({
            "name":"Lead Jams Display",
            "string":expected_lead_jammer,
            "location":self.browser.find_element_by_id(
                'id_lead_jams').get_attribute('innerHTML'),
            "message":"'{0}' not found in id_lead_jams".format(
                expected_lead_jammer)
        })
        
        self.expected_elements.append({
            "name":"Jams as Blocker Display",
            "string":expected_blocker,
            "location":self.browser.find_element_by_id(
                'id_blocker_jams').get_attribute('innerHTML'),
            "message":"'{0}' not found in id_blocker_jams".format(
                expected_blocker)
        })

        self.expected_elements.append({
            "name":"Jams as Pivot Display",
            "string":expected_pivot,
            "location":self.browser.find_element_by_id(
                'id_pivot_jams').get_attribute('innerHTML'),
            "message":"'{0}' not found in id_pivot_jams".format(expected_pivot)

        })

        self.expected_elements.append({
            "name":"Blocker Name Display",
            "string":expected_name,
            "location":self.browser.find_element_by_id(
                'id_player_name').get_attribute('innerHTML'),
            "message":"'{0}' not found in id_player_name".format(expected_name)
        })

        self.expected_elements.append({
            "name":"Bouts Played Display",
            "string":expected_bouts,
            "location":self.browser.find_element_by_id(
                'id_bouts').get_attribute('innerHTML'),
            "message":"'{0}' not found in id_bouts".format(expected_bouts)
        })

        self.__verify_expected_elements()

