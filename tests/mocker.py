from random import choices
from datetime import datetime
from pyrecard.subscription import plan, customer


def mock_plan():
    '''
       The following data has been taken and adapted from
       https://dev.wirecard.com.br/v1.5/reference#criar-plano
    '''
    return {
        'code': ''.join(choices('ABCDEF1234567890', k=10)),
        'name': 'Plano Especial',
        'description': 'Descrição do Plano Especial',
        'amount': 990,
        'setup_fee': 500,
        'max_qty': 1,
        'interval': {'length': 1, 'unit': 'MONTH'},
        'billing_cycles': 12,
        'payment_method': 'ALL'
    }


def mock_customer():
    '''
       The following data has been taken and adapted from
       https://dev.wirecard.com.br/v1.5/reference#criar-assinante
    '''
    return {
        'code': ''.join(choices('ABCDEF1234567890', k=10)),
        'email': 'test@user.com',
        'fullname': 'Test User',
        'cpf': '36598211018',  # cpf obtained in https://www.4devs.com.br/gerador_de_cpf
        'phone_area_code': '11',
        'phone_number': '934343434',
        'birthdate_day': '26',
        'birthdate_month': '04',
        'birthdate_year': '1980',
        'address': {
            'street': 'Street Name',
            'number': '100',
            'complement': '',
            'district': 'Neighboor Name',
            'city': 'City Name',
            'state': 'MG',
            'country': 'BRA',
            'zipcode': '00000000',
        },
        'billing_info': {
            'credit_card': {
                'holder_name': 'Test User',
                'number': '4111111111111111',
                'expiration_month': '06',
                'expiration_year': str(datetime.now().year+2)[2:]
            }
        }
    }


def mock_subscription():
    '''
       The following data has been taken and adapted from
       https://dev.wirecard.com.br/v1.5/reference#assinaturas
    '''
    mocked_plan = mock_plan()
    mocked_customer = mock_customer()
    plan.create(mocked_plan)
    customer.create(mocked_customer, new_vault=True)
    return {
        'code': ''.join(choices('ABCDEF1234567890', k=10)),
        'amount': 9990,
        'payment_method': 'CREDIT_CARD',
        'plan': {'code': mocked_plan['code']},
        'customer': {'code': mocked_customer['code']},
    }
