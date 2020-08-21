from pyrecard.utils.pyrequest import pyrequest


def fetch_invoice(code):
    return pyrequest('GET', f'/invoices/{code}')


def fetch_invoice_payments(code):
    return pyrequest('GET', f'/invoices/{code}/payments')


def payment_details(code):
    return pyrequest('GET', f'/payments/{code}')


def payment_retry(code):
    return pyrequest('POST', f'/payments/{code}')
