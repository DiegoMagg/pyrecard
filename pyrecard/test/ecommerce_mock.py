from random import choices
from pyrecard.ecommerce import customer
from datetime import datetime


def mock_client():
    code = ''.join(choices('ABCDEF1234567890', k=10))
    return {
        'ownId': code,
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


def mock_credit_card():
    return {
        'method': 'CREDIT_CARD',
        'creditCard': {
            'expirationMonth': '05',
            'expirationYear': str(datetime.now().year+2)[2:],
            'number': '4012001037141112',
            'cvc': '123',
            'holder': {
                'fullname': 'João Silva',
                'birthdate': '1990-10-22',
                'taxDocument': {'type': 'CPF', 'number': '22288866644'},
                'phone': {'countryCode': '55', 'areaCode': '11', 'number': '55552266'},
            }
        }
    }


def mock_order():
    response = customer.create(mock_client())
    return {
        'ownId': f'ORDER-{"".join(choices("ABCDEF1234567890", k=10))}',
        'amount': {'currency': 'BRL', 'subtotals': {'shipping': 1500}},
        'items': [
            {
                'product': 'Descrição do pedido',
                'category': 'CLOTHING',
                'quantity': 1,
                'detail': 'Camiseta estampada branca',
                'price': 9500
            }
        ],
        'customer': {'id': response.json()['id']},
    }
