from pyrecard.utils.pyrequest import pyrequest


def fetch_invoice(code):
    return pyrequest('GET', f'/invoices/{code}')


def fetch_invoice_payments(code):
    return pyrequest('GET', f'/invoices/{code}/payments')


def payment_details(code):
    return pyrequest('GET', f'/payments/{code}')


def retry_invoice_payment(code):
    return pyrequest('POST', f'/invoices/{code}/retry')


def generate_bank_slip(code, json={}):
    return pyrequest('POST', f'/invoices/{code}/boletos', json)
