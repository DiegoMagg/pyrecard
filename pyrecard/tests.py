import unittest
from os import environ
from datetime import datetime
import requests
from random import choices
from pyrecard.signature import plans, customer
from exceptions import MissingKey
from common.urls import get_url


class PlanTestCase(unittest.TestCase):
    '''
       The following data has been taken and adapted from
       https://dev.wirecard.com.br/v1.5/reference#criar-plano
    '''

    def setUp(self):
        environ['WIRECARD_KEY'] = '01010101010101010101010101010101:ABABABABABABABABABABABABABABABABABABABAB'
        self.data = {
            'code': ''.join(choices('ABCDEF1234567890', k=10)),
            'name': 'Plano Especial',
            'description': 'Descrição do Plano Especial',
            'amount': 990,
            'setup_fee': 500,
            'max_qty': 1,
            'interval': {'length': 1, 'unit': 'MONTH'},
            'billing_cycles': 12,
            'payment_method': 'CREDIT_CARD'
        }

    def test_wirecard_sandbox_must_be_accessible(self):
        response = requests.get(get_url())
        self.assertEqual(401, response.status_code)
        self.assertEqual('Token or Key are invalids', response.json()['ERROR'])

    def test_raise_error_if_key_is_missing(self):
        environ['WIRECARD_KEY'] = ''
        with self.assertRaises(MissingKey):
            plans.create(self.data)

    def test_plan_with_valid_data_should_be_created(self):
        response = plans.create(self.data)
        self.assertEqual(response.status_code, 201)

    def test_plan_with_invalid_data_should_not_be_created(self):
        self.data['code'] = ''
        response = plans.create(self.data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('errors' in response.json())

    def test_plan_should_be_changed(self):
        plans.create(self.data)
        old_amount = self.data['amount']
        self.data['amount'] = 1000
        code = self.data.pop('code')
        plans.alter(code, self.data)
        response = plans.fetch(code)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json().get('amount'), old_amount)

    def test_all_plans_must_be_returned(self):
        response = plans.fetch_all()
        self.assertEqual(response.status_code, 200)
        self.assertTrue('plans' in response.json())
        self.assertGreater(len(response.json()['plans']), 1)

    def test_plan_must_be_inactivated_and_reactivated(self):
        plans.create(self.data)
        response = plans.fetch(self.data['code'])
        self.assertEqual(response.json()['status'], 'ACTIVE')
        plans.inactivate(self.data['code'])
        response = plans.fetch(self.data['code'])
        self.assertNotEqual(response.json()['status'], 'ACTIVE')
        plans.activate(self.data['code'])
        response = plans.fetch(self.data['code'])
        self.assertEqual(response.json()['status'], 'ACTIVE')


class CustomersTestCase(unittest.TestCase):
    '''
       The following data has been taken and adapted from
       https://dev.wirecard.com.br/v1.5/reference#criar-assinante
    '''

    def setUp(self):
        environ['WIRECARD_KEY'] = '01010101010101010101010101010101:ABABABABABABABABABABABABABABABABABABABAB'
        self.data = {
            'code': ''.join(choices('ABCDEF1234567890', k=10)),
            'email': 'test@user.com',
            'fullname': 'Test User',
            'cpf': '22222222222',
            'phone_area_code': '11',
            'phone_number': '934343434',
            'birthdate_day': '26',
            'birthdate_month': '04',
            'birthdate_year': '1980',
            'address': {
                'street': 'Street Name',
                'number': '100',
                'complement': '',
                'district': 'Neighboor Name',
                'city': 'City Name',
                'state': 'MG',
                'country': 'BRA',
                'zipcode': '00000000',
            },
            'billing_info': {
                'credit_card': {
                    'holder_name': 'Test User',
                    'number': '4111111111111111',
                    'expiration_month': '06',
                    'expiration_year': str(datetime.now().year+2)[2:]
                }
            }
        }

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
