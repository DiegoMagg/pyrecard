import unittest
from tests import subscription_tests, factory_tests, ecommerce_tests

MODULES = (factory_tests, subscription_tests, ecommerce_tests)


if __name__ == "__main__":
    for module in MODULES:
        print(f'Starting {module.__name__}')
        suite = unittest.TestLoader().loadTestsFromModule(module)
        unittest.TextTestRunner(verbosity=1).run(suite)
