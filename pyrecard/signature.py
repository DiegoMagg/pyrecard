import requests
from common.auth import authorization


class Plan:

    def __init__(self, json):
        self.json = json
        self.url = 'https://sandbox.moip.com.br/assinaturas/v1/plans'

    @authorization
    def create(self, headers):
        response = requests.post(self.url, headers=headers, json=self.json)
        return {**{'status_code': response.status_code}, **response.json()}

    # def alter(self):
    #     response = requests.put(self.coded_url, headers=HEADERS, json=self.parse_plan())
    #     return response.status_code

    # def deactivate(self):
    #     response = requests.put(self.deactivate_url, headers=HEADERS)
    #     return response.status_code

    # def activate(self):
    #     response = requests.put(self.activate_url, headers=HEADERS)
    #     return response.status_code

    # def fetch(self):
    #     response = requests.get(self.coded_url, headers=HEADERS)
    #     return response.json() if response.ok else {}

    # @staticmethod
    # def fetch_all():
    #     response = requests.get(f'{settings.MOIP_URL}/plans/', headers=HEADERS)
    #     return response.json().get('plans')

    # def parse_plan(self):
    #     return {
    #         'code': self.plan.mexase_id, 'name': self.plan.nome, 'amount': int(self.plan.mensalidade * 100),
    #         'setup_fee': int(self.plan.taxa_matricula * 100), 'interval': {'length': 1, 'unit': 'MONTH'},
    #         'payment_method': 'ALL', 'active': self.plan.ativo,
    #     }
