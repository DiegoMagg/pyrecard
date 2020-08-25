from pyrecard.utils.pyrequest import pyrequest


def preferences(url, email_merchant_enabled, customer_enabled):
    data = {
        'notification': {
            'webhook': {'url': url},
            'email': {
                'merchant': {'enabled': email_merchant_enabled},
                'customer': {'enabled': customer_enabled},
            }
        }
    }
    return pyrequest('POST', '/assinaturas/v1/users/preferences', data)
