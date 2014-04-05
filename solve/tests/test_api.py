from django.contrib.auth.models import User
from tastypie.test import ResourceTestCase
from solve.models import Equation


class CalculatorResourceTest(ResourceTestCase):

    def setUp(self):
        super(CalculatorResourceTest, self).setUp()

        # Create a user.
        self.username = 'daniel'
        self.password = 'pass'
        self.user = User.objects.create_superuser(self.username, 'daniel@example.com', self.password)
        self.user1 = User.objects.create_superuser('juan', 'juan@example.com', 'pass')
        # We also build a detail URI, since we will be using it all over.
        # DRY, baby. DRY.
        self.api_url = '/api/v1/'
        self.calculator_url = self.api_url + 'calculator/'
        self.session_url = self.api_url + 'session/'
        # login user
        self.api_client.client.login(username=self.username, password=self.password)

    def test_get_list_json(self):
        resp = self.api_client.get(self.calculator_url, format='json')
        self.assertValidJSONResponse(resp)
        # Scope out the data for correctness.
        self.assertEqual(len(self.deserialize(resp)['objects']), 0)

    def _create_equation(self, equation):
        post_data = {'equation': '2*log(10)+1'}
        self.assertHttpCreated(self.api_client.post(self.calculator_url, format='json', data=post_data))

    def test_create_equation(self):
        # Check how many are there first.
        self.assertEqual(Equation.objects.count(), 0)
        self._create_equation('2*log(10)+1')
        # Verify a new one has been added.
        self.assertEqual(Equation.objects.count(), 1)

    def test_save_session(self):
        # Create two equations
        self._create_equation('2*log(10)+1')
        self._create_equation('1+1')
        self.assertEqual(len(Equation.objects.all()), 2)
        # save session
        post_data = {'name': 'session1'}
        self.api_client.post(self.session_url, format='json', data=post_data)
        # check equations
        self.assertEqual(len(Equation.objects.filter(session__name='session1')), 2)

    def test_load_session(self):
        # Create two equations
        self._create_equation('2*log(10)+1')
        self._create_equation('1+1')
        # save equations
        post_data = {'name': 'session1'}
        self.api_client.post(self.session_url, format='json', data=post_data)
        # load equations
        resp = self.api_client.get(self.calculator_url, format='json',
            data={'session__name': 'session1'})
        self.assertValidJSONResponse(resp)
        # Scope out the data for correctness.
        self.assertEqual(len(self.deserialize(resp)['objects']), 2)

    def test_multi_user_session(self):
        # Create equations for one user
        self.test_load_session()
        # login a differen user
        self.api_client.client.login(username='juan', password='pass')
        self.test_load_session()
        self.assertEqual(len(Equation.objects.filter(session__name='session1')), 4)

