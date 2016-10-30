import warnings

from django.core.urlresolvers import reverse
from django_webtest import WebTest

from wftda_importer import factories
from wftda_importer.models import Bout, PlayerToJam, Jam

class StatDetailPage(WebTest):
    """Open up a page and it's got stats for Jill Nye across multiple available
bouts
    """
    def setUp(self):
        self.url = [reverse('display_stats'),]
        
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
                self.assertIn(test['string'], test['location'], 
                        msg=test['message'])

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
            "lead":PlayerToJam.objects.filter(player=p2, 
                lead_flag=True).count(),
            "no_lead":PlayerToJam.objects.filter(player=p2, 
                lead_flag=False).count()
        }

        calculated_stats = {
            "lead_percentage":
            (100 * status['lead']/position['jammer']) \
                if position['jammer'] !=0 else 0,
        }

        # Create strings to look for in page HTML
        expected_blocker = "blocker jams: {0}".format(position['blocker'])
        expected_pivot = "pivot jams: {0}".format(position['pivot'])
        expected_jammer = "jammer jams: {0}".format(position['jammer'])
        expected_lead_jammer = "lead jammer: {0}".format(status['lead'])
        expected_lead_percentage = "lead percentage: {0}".format(
            calculated_stats['lead_percentage'])
        expected_name = p2.name
        expected_title_string = "Stats for {0}".format(expected_name)
        expected_bouts = "bouts: {0}".format(Bout.objects.filter(
            home_roster__players=p2).count())

        self.url.append('{0}/'.format(p2.id))
        result = self.app.get(''.join(self.url))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            #This causes a Unicode warning, not sure why, nofix for now
            html = result.html

        self.expected_elements.append({
            "name":"Detail Page Title",
            "string":expected_title_string,
            "location":html.title,
            "message":
                "'{0}' not found in browser title for player id {1}".format(
                expected_title_string, p2.id)
        })

        expected_jams_played = "jams: {0}".format(
            position['blocker']+position['pivot']+position['jammer'])
        self.expected_elements.append({
            "name":"Jams Played Display",
            "string":expected_jams_played,
            "location":html.find(id='id_played_jams').contents[0],
            "message":"'{0}' not found in id_played_jams".format(
                expected_jams_played), 
        })


        total_jams_available = "total jams available: {0}".format(
                total_jams_available_p2)
        self.expected_elements.append({
            "name":"Total Jams Available to Player Display",
            "string":total_jams_available,
            "location":html.find(id='id_total_jams_available').contents[0],
            "message":"'{0}' not found in id_total_jams_available".format(
                total_jams_available)
        })

        self.expected_elements.append({
            "name":"Jams as Jammer Display",
            "string":expected_jammer,
            "location":html.find(id='id_jammer_jams').contents[0],
            "message":"'{0}' not found in id_jammer_jams".format(
                expected_jammer)
        })
        
        self.expected_elements.append({
            "name":"Lead Jams Display",
            "string":expected_lead_jammer,
            "location":html.find(id='id_lead_jams').contents[0],
            "message":"'{0}' not found in id_lead_jams".format(
                expected_lead_jammer)
        })
        
        self.expected_elements.append({
            "name":"Jams as Blocker Display",
            "string":expected_blocker,
            "location":html.find(id='id_blocker_jams').contents[0],
            "message":"'{0}' not found in id_blocker_jams".format(
                expected_blocker)
        })


        self.expected_elements.append({
            "name":"Jams as Pivot Display",
            "string":expected_pivot,
            "location":html.find(id='id_pivot_jams').contents[0],
            "message":"'{0}' not found in id_pivot_jams".format(expected_pivot)

        })

        self.expected_elements.append({
            "name":"Blocker Name Display",
            "string":expected_name,
            "location":html.find(id='id_player_name').contents[0],
            "message":"'{0}' not found in id_player_name".format(expected_name)
        })

        self.expected_elements.append({
            "name":"Bouts Played Display",
            "string":expected_bouts,
            "location":html.find(id='id_bouts').contents[0],
            "message":"'{0}' not found in id_bouts".format(expected_bouts)
        })

        self.expected_elements.append({
            "name":"Lead Jammer Percentage Display",
            "string":expected_lead_percentage,
            "location":html.find(id='id_lead_percentage').contents[0],
            "message":"'{0}' not found in id_lead_percentage".format(
                expected_lead_percentage)
        })

        self.__verify_expected_elements()

