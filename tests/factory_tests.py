import unittest
from os import environ
from pyrecard.exceptions import MissingKey, InvalidKey
from pyrecard.utils.factory import b64_factory, header_factory


class FactoryTestCase(unittest.TestCase):

    def test_raise_error_if_not_key(self):
        with self.assertRaises(MissingKey):
            b64_factory(None)

    def test_raise_error_if_key_is_invalid(self):
        with self.assertRaises(InvalidKey):
            b64_factory('1010:ABAB')

    def test_generate_b64_object_with_a_valid_key(self):
        header = b64_factory(environ.get('SANDBOX_KEY'))
        self.assertTrue('Authorization' in header)
        self.assertTrue('Basic' in header['Authorization'])

    def test_header_with_authorization_must_be_returned_in_sandbox(self):
        '''
           if the environment variable "PYRECARD_ENV" isn't to "production"
           then the key used will be "SANDBOX_KEY" will be used.
        '''
        headers = header_factory()
        self.assertTrue('User-Agent' in headers)
        self.assertTrue('Authorization' in headers)

    def test_header_with_authorization_must_be_returned_in_production(self):
        '''
           if the environment variable "PYRECARD_ENV" is set to "production"
           then the key used will be "PRODUCTION_KEY".
        '''
        environ['PRODUCTION_KEY'] = environ.get('SANDBOX_KEY')
        environ['PYRECARD_ENV'] = 'production'
        headers = header_factory()
        self.assertTrue('User-Agent' in headers)
        self.assertTrue('Authorization' in headers)

    def tearDown(self):
        environ['PYRECARD_ENV'] = ''
