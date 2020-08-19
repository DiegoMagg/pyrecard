import unittest
from tests import subscription_tests, common_tests
from os import environ


MODULES = (common_tests, subscription_tests)

# Key obtained from wirecard documentation
environ['SANDBOX_KEY'] = '01010101010101010101010101010101:ABABABABABABABABABABABABABABABABABABABAB'

if __name__ == "__main__":
    for module in MODULES:
        print(f'Starting {module.__name__}')
        suite = unittest.TestLoader().loadTestsFromModule(module)
        unittest.TextTestRunner(verbosity=1).run(suite)
