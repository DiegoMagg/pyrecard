from random import choices
from datetime import datetime


def mock_client():
    code = ''.join(choices('ABCDEF1234567890', k=10))
    return {
        'ownId': f'CUSTOMER-{code}',
        'fullname': f'Cliente {code}',
        'email': f'{code}@email.com',
        'birthDate': '1980-5-10',
        'taxDocument': {
            'type': 'CPF',
            'number': '10013390023'
        },
        'phone': {
            'countryCode': '55',
            'areaCode': '11',
            'number': '22226842'
        },
        'shippingAddress': {
            'city': 'Rio de Janeiro',
            'district': 'Ipanema',
            'street': 'Avenida Atlântica',
            'streetNumber': '60',
            'zipCode': '02446000',
            'state': 'RJ',
            'country': 'BRA'
        },
        'fundingInstrument': {
            'method': 'CREDIT_CARD',
            'creditCard': {
                'expirationMonth': '06',
                'expirationYear': str(datetime.now().year+2)[2:],
                'number': '6362970000457013',
                'cvc': '123',
                'holder': {
                    'fullname': f'Cliente {code}',
                    'birthdate': '1980-05-10',
                    'taxDocument': {
                        'type': 'CPF',
                        'number': '10013390023'
                    },
                    'billingAddress': {
                        'city': 'São Paulo',
                        'district': 'Jardim Paulistano',
                        'street': 'Avenida Brigadeiro Faria Lima',
                        'streetNumber': '123',
                        'zipCode': '01451000',
                        'state': 'SP',
                        'country': 'BRA'
                    },
                    'phone': {
                        'countryCode': '55',
                        'areaCode': '11',
                        'number': '22226842'
                    }
                }
            }
        }
    }
