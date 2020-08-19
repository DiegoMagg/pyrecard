'''Module containing exceptions raised by pyrecard.'''


class PyrecardException(Exception):
    '''Base class for all exceptions raised by pyrecard.'''

    pass


class MissingKey(PyrecardException):
    '''Raised when wirecard key is missing'''

    pass


class InvalidKey(PyrecardException):
    '''Raised when wirecard key is invalid'''

    pass
