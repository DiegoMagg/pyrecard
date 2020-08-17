import unittest
from os import environ
from random import choices
from .signature import Plan
from exceptions import MissingKey


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

    def test_raise_error_if_key_is_missing(self):
        environ['WIRECARD_KEY'] = ''
        with self.assertRaises(MissingKey):
            new_plan = Plan(self.data)
            new_plan.create()

    def test_plan_with_valid_data_should_be_created(self):
        new_plan = Plan(self.data)
        response = new_plan.create()
        self.assertEqual(response.get('status_code'), 201)
        self.assertEqual(response.get('message'), 'Plano criado com sucesso')

    def test_plan_with_invalid_data_should_not_be_created(self):
        self.data['code'] = ''
        new_plan = Plan(self.data)
        response = new_plan.create()
        self.assertEqual(response.get('status_code'), 400)
        self.assertEqual(response.get('message'), 'Erro na requisição')
