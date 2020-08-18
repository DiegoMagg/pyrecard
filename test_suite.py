import unittest
from tests import signature_tests


MODULES = (signature_tests,)

if __name__ == "__main__":
    for module in MODULES:
        print(f'Starting {module.__name__}')
        suite = unittest.TestLoader().loadTestsFromModule(module)
        unittest.TextTestRunner(verbosity=1).run(suite)
