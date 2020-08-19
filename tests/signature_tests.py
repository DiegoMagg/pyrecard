import unittest
from os import environ
import requests
from pyrecard.signature import plan, customer, subscription
from exceptions import MissingKey
from common.urls import get_url
from tests.mocker import mock_plan, mock_customer, mock_subscription


environ['WIRECARD_KEY'] = '01010101010101010101010101010101:ABABABABABABABABABABABABABABABABABABABAB'


class PlanTestCase(unittest.TestCase):
    '''
       The following data has been taken and adapted from
       https://dev.wirecard.com.br/v1.5/reference#criar-plano
    '''

    def setUp(self):
        self.data = mock_plan()

    def test_wirecard_sandbox_must_be_accessible(self):
        response = requests.get(get_url())
        self.assertEqual(401, response.status_code)
        self.assertEqual('Token or Key are invalids', response.json()['ERROR'])

    def test_raise_error_if_key_is_missing(self):
        environ['WIRECARD_KEY'] = ''
        with self.assertRaises(MissingKey):
            plan.create(self.data)

    def test_plan_with_valid_data_should_be_created(self):
        response = plan.create(self.data)
        self.assertEqual(response.status_code, 201)

    def test_plan_with_invalid_data_should_not_be_created(self):
        self.data['code'] = ''
        response = plan.create(self.data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('errors' in response.json())

    def test_plan_should_be_changed(self):
        plan.create(self.data)
        old_amount = self.data['amount']
        self.data['amount'] = 1000
        code = self.data.pop('code')
        plan.alter(code, self.data)
        response = plan.fetch(code)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json().get('amount'), old_amount)

    def test_all_plans_must_be_returned(self):
        response = plan.fetch_all()
        self.assertEqual(response.status_code, 200)
        self.assertTrue('plans' in response.json())
        self.assertGreater(len(response.json()['plans']), 1)

    def test_plan_must_be_inactivated_and_reactivated(self):
        plan.create(self.data)
        response = plan.fetch(self.data['code'])
        self.assertEqual(response.json()['status'], 'ACTIVE')
        plan.inactivate(self.data['code'])
        response = plan.fetch(self.data['code'])
        self.assertNotEqual(response.json()['status'], 'ACTIVE')
        plan.activate(self.data['code'])
        response = plan.fetch(self.data['code'])
        self.assertEqual(response.json()['status'], 'ACTIVE')

    def tearDown(self):
        environ['WIRECARD_KEY'] = '01010101010101010101010101010101:ABABABABABABABABABABABABABABABABABABABAB'


class CustomersTestCase(unittest.TestCase):
    '''
       The following data has been taken and adapted from
       https://dev.wirecard.com.br/v1.5/reference#criar-assinante
    '''

    def setUp(self):
        self.data = mock_customer()

    def test_customer_with_valid_data_must_be_created(self):
        response = customer.create(self.data)
        self.assertEqual(response.status_code, 201)

    def test_customer_must_be_changed(self):
        customer.create(self.data)
        old_street_name = self.data['address']['street']
        self.data['address']['street'] = 'New Street Name'
        customer.alter(self.data['code'], self.data)
        response = customer.fetch(self.data['code'])
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json()['address']['street'], old_street_name)

    def test_all_customers_must_be_returned(self):
        response = customer.fetch_all()
        self.assertEqual(response.status_code, 200)
        self.assertTrue('customers' in response.json())
        self.assertGreater(len(response.json()['customers']), 1)

    def test_credit_card_must_be_changed(self):
        customer.create(self.data)
        credit_card = self.data['billing_info']
        credit_card['credit_card']['number'] = '5555666677778884'
        response = customer.change_card(self.data['code'], credit_card)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('message' in response.json())


class SubscriptionTestCase(unittest.TestCase):
    '''
       The following data has been taken and adapted from
       https://dev.wirecard.com.br/v1.5/reference#assinaturas
    '''

    def setUp(self):
        self.data = mock_subscription()

    def test_signature_must_be_created(self):
        response = subscription.create(self.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], 'Assinatura criada com sucesso')

    def test_signature_must_be_created_with_new_customer(self):
        self.data['customer'] = mock_customer()
        response = subscription.create(self.data, True)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], 'Assinatura criada com sucesso')

    def test_subscription_details_must_be_returned(self):
        subscription.create(self.data)
        response = subscription.fetch(self.data['code'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], self.data['code'])

    def test_all_subscriptions_must_be_returned(self):
        response = subscription.fetch_all()
        self.assertEqual(response.status_code, 200)
        self.assertTrue('subscriptions' in response.json())
        self.assertGreater(len(response.json()['subscriptions']), 1)

    def test_subscription_status_must_changed(self):
        subscription.create(self.data)
        response = subscription.set_status(self.data['code'], 'suspend')
        self.assertEqual(response.status_code, 200)
        response = subscription.set_status(self.data['code'], 'activate')
        self.assertEqual(response.status_code, 200)
        response = subscription.set_status(self.data['code'], 'cancel')
        self.assertEqual(response.status_code, 200)

    def test_subscription_data_must_be_changed(self):
        subscription.create(self.data)
        data = mock_plan()
        plan.create(data)
        self.data['plan']['code'] = data['code']
        code = self.data.pop('code')
        del self.data['customer']
        response = subscription.change(code, self.data)
        self.assertEqual(response.status_code, 200)

    def test_subscription_payment_method_must_be_changed(self):
        subscription.create(self.data)
        response = subscription.set_payment_method(self.data['code'], 'BOLETO')
        self.assertEqual(response.status_code, 200)