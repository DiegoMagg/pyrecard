from pyrecard.utils.pyrequest import pyrequest


INVOICE_PATH = '/assinaturas/v1/invoices'


def fetch_invoice(code):
    return pyrequest('GET', f'{INVOICE_PATH}/{code}')


def fetch_invoice_payments(code):
    return pyrequest('GET', f'{INVOICE_PATH}/{code}/payments')


def payment_details(code):
    return pyrequest('GET', f'/assinaturas/v1/payments/{code}')


def retry_invoice_payment(code):
    return pyrequest('POST', f'{INVOICE_PATH}/{code}/retry')


def generate_bank_slip(code, json={}):
    return pyrequest('POST', f'{INVOICE_PATH}/{code}/boletos', json)
