from pyrecard.utils.pyrequest import pyrequest


def fetch_invoice(invoice_id):
    return pyrequest('GET', f'/invoices/{invoice_id}')


def fetch_invoice_payments(invoice_code):
    return pyrequest('GET', f'/invoices/{invoice_code}/payments')


def payment_details(payment_code):
    return pyrequest('GET', f'/payments/{payment_code}')


def retry_invoice_payment(invoice_code):
    return pyrequest('POST', f'/invoices/{invoice_code}/retry')


def generate_bank_slip(invoice_code, json={}):
    return pyrequest('POST', f'/invoices/{invoice_code}/boletos', json)
