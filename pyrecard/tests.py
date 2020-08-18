import unittest
from os import environ
import requests
from random import choices
from pyrecard.signature import plans
from exceptions import MissingKey
from common.auth import get_auth_header


class PlanTestCase(unittest.TestCase):

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

    def test_wirecard_plan_must_be_acessible(self):
        self.assertEqual(200, requests.get(plans.URL, headers=get_auth_header()).status_code)

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
        response = plans.create(self.data)
        old_amount = self.data['amount']
        self.data['amount'] = 1000
        code = self.data.pop('code')
        response = plans.alter(code, self.data)
        fetch_data = plans.fetch(code)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(fetch_data.json().get('amount'), old_amount)
