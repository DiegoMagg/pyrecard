from random import choices
from datetime import datetime
from pyrecard.subscription import plan, customer


def plan_data():
    '''
       The following data has been taken and adapted from
       https://dev.wirecard.com.br/v1.5/reference#criar-plano
    '''
    code = ''.join(choices('ABCDEF1234567890', k=10))
    return {
        'code': code,
        'name': f'Plano {code}',
        'description': f'Descrição do Plano {code}',
        'amount': 990,
        'setup_fee': 500,
        'max_qty': 1,
        'interval': {'length': 1, 'unit': 'MONTH'},
        'billing_cycles': 12,
        'payment_method': 'ALL'
    }


def customer_data():
    '''
       The following data has been taken and adapted from
       https://dev.wirecard.com.br/v1.5/reference#criar-assinante
    '''
    code = ''.join(choices('ABCDEF1234567890', k=10))
    return {
        'code': code,
        'email': f'cliente{code}@provedor.com',
        'fullname': f'Usuário {code}',
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


def subscription_data():
    '''
       The following data has been taken and adapted from
       https://dev.wirecard.com.br/v1.5/reference#assinaturas
    '''
    mocked_plan = plan_data()
    mocked_customer = customer_data()
    plan.create(mocked_plan)
    customer.create(mocked_customer, new_vault=True)
    return {
        'code': ''.join(choices('ABCDEF1234567890', k=10)),
        'amount': 9990,
        'payment_method': 'CREDIT_CARD',
        'plan': {'code': mocked_plan['code']},
        'customer': {'code': mocked_customer['code']},
    }


def coupon_data():
    '''
       The following data has been taken and adapted from
       https://dev.wirecard.com.br/v1.5/reference#criar-coupon
    '''
    code = ''.join(choices('ABCDEF1234567890', k=10))
    return {
        'code': f'coupon-{code}',
        'name': f'Coupon {code}',
        'description': 'My new coupon',
        'discount': {
            'value': 10000,
            'type': 'percent'
        },
        'status': 'active',
        'duration': {
            'type': 'repeating',
            'occurrences': 12
        },
        'max_redemptions': 1000,
        'expiration_date': {
            'year': datetime.now().year,
            'month': datetime.now().month,
            'day': datetime.now().day,
        }
    }
