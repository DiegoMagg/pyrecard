import unittest
from pyrecard.ecommerce import customer
from pyrecard.test.ecommerce_mock import mock_client, mock_credit_card, mock_order


class CustomerTestCase(unittest.TestCase):

    def setUp(self):
        self.data = mock_client()
        self.card_data = mock_credit_card()
        self.order_data = mock_order()

    def test_customer_must_be_created(self):
        response = customer.create(self.data)
        self.assertTrue(response.ok)
        self.assertTrue('id' in response.json())

    def test_credit_card_must_be_added_correctly(self):
        del self.data['fundingInstrument']
        self.assertFalse(self.data.get('fundingInstrument'))
        customer.create(self.data)
        response = customer.add_credit_card(self.data['ownId'], self.card_data)
        self.assertTrue(response.ok)
        self.assertTrue('brand' in response.json()['card'])

    def test_customer_data_must_be_returned(self):
        user_id = customer.create(self.data).json()['id']
        response = customer.fetch(user_id)
        self.assertTrue(response.ok)
        self.assertTrue('_links' in response.json())

    def test_credit_card_must_be_deleted(self):
        user = customer.create(self.data).json()
        credit_card_id = user['fundingInstruments'][0]['creditCard']['id']
        response = customer.remove_credit_card(credit_card_id)
        self.assertTrue(response.ok)
        response = customer.fetch(user['id'])
        self.assertFalse('fundingInstruments' in response.json())

    def test_all_customers_must_be_returned(self):
        response = customer.fetch_all()
        self.assertTrue(response.ok)
        self.assertTrue('customers' in response.json())
        self.assertIsInstance(response.json()['customers'], list)
