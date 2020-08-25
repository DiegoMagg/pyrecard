# Pyrecard

![pipy](https://img.shields.io/pypi/v/pyrecard)
![pyver](https://img.shields.io/badge/python-3.6%2B-blue)
[![Build Status](https://travis-ci.com/DiegoMagg/pyrecard.svg?token=tABSMskBskhEHyyfYxzM&branch=master)](https://github.com/DiegoMagg/pyrecard)
[![codecov](https://codecov.io/gh/DiegoMagg/pyrecard/branch/master/graph/badge.svg?token=RT3ZXODSAH)](https://codecov.io/gh/DiegoMagg/pyrecard)

A Python lib for brazilian [Wirecard](https://wirecard.com.br/) payment gateway.

Wirecard works with a base64 hash made up of its `TOKEN:KEY` in its operations. Pyrecard uses two environment variables with these sets `SANDBOX_KEY` and `PRODUCTION_KEY` and generates the necessary hash for an operation. This lib works in SANDBOX by default, to use PRODUCTION mode set environment variable `PYRECARD_ENV=production`

Currently working with **subscriptions** only.

**Table of Contents**

1. Installation
2. Usage
3. Used by

## Installation

Minimal setup:

```shell
$ pip install pyrecard
$ export SANDBOX_KEY=TOKEN:KEY
$ export PRODUCTION_KEY=TOKEN:KEY
```

Setup with [pipenv](https://pipenv.pypa.io/en/latest/) (recomended):

```shell
$ pipenv install pyrecard
```

Create a `.env` file with required data:

    SANDBOX_KEY=TOKEN:KEY
    PRODUCTION_KEY=TOKEN:KEY

## Usage
### subscriptions.plan
The **plan** module performs the following operations:

- plan.create(json)
- plan.alter(plan_code, json)
- plan.activate(plan_code)
- plan.inactivate(plan_code)
- plan.fetch(plan_code)
- plan.fetch_all()

All operations above returns a response.

```python
>>> from pyrecard.subscription import plan
>>> response = plan.fetch("plan101")
>>> response
<Response [200]>
>>> response.json()
{'setup_fee': 500, 'amount': 990, 'code': 'plan101', 'name': 'Plano Especial', 'billing_cycles': 12, 'description': 'Descrição do PlanoEspecial', 'interval': {'unit': 'MONTH', 'length': 1}, 'creation_date': {'month': 1, 'hour': 0, 'year': 2016, 'day': 8, 'minute': 0, 'second':0}, 'payment_method': 'CREDIT_CARD', 'max_qty': 1, 'trial': {'hold_setup_fee': True, 'days': 30, 'enabled': True}, 'status': 'ACTIVE'}
>>>
```

### subscriptions.customer

The **customer** module performs the following operations:

- customer.create(json, new_vault=False)
- customer.alter(customer_code, json)
- customer.fetch(customer_code)
- customer.fetch_all()
- customer.change_card(customer_code, json)

Set `new_vault` True to create a user with billing data.

```python
>>> from pyrecard.subscription import customer
>>> customer_data = customer.fetch('cliente01').json()
>>> customer_data['address']['state'] = 'MG'
>>> response = customer.alter('cliente01', customer_data)
>>> response
<Response [200]>
```

### subscription.subscription

The **subscription** module performs the following operations:

- subscription.create(json, new_customer=False)
- subscription.alter(subscription_code, json)
- subscription.fetch(subscription_code)
- subscription.fetch_all()
- subscription.set_status(subscription_code, status)
- subscription.set_payment_method(subscription_code, method)
- subscription.fetch_all_invoices(subscription_code)

Set `new_customer` True to create a subscription with a new user.

`set_status` allows `suspend`, `activate` or `cancel`

`set_payment_method` allows `CREDIT_CARD` or `BOLETO`

```python
>>> from pyrecard.subscription import subscription
>>> response = subscription.set_status('assinatura01',  'suspend')
>>> response
<Response [200]>
```

More information check the [subscription documentation](https://dev.wirecard.com.br/v1.5/reference#assinaturas)

### subscription.payment

The **payment** module performs the following operations:

- payment.fetch_invoice(invoice_id)
- payment.fetch_invoice_payments(invoice_code)
- payment.payment_details(payment_code)
- payment.retry_invoice_payment(invoice_code)
- payment.generate_bank_slip(invoice_code, json)

```python
>>> from pyrecard.subscription import payment
>>> response = payment.fetch_invoice('1025240')
>>> response
<Response [200]>
>>> response.json()
{'subscription_code': 'assinatura01', 'amount': 0, 'id': 1025240, 'creation_date': {'month': 1, 'hour': 14, 'year': 2016, 'day': 8, 'minute':28, 'second': 52}, 'occurrence': 1, 'plan': {'code': 'plan101', 'name': 'Plano Especial'}, 'items': [{'amount': 0, 'type': 'Período de trial'}, 'customer': {'code': 'cliente03', 'fullname': 'Nome Sobrenome', 'email': 'nome@exemplo.com.br'}, 'status': {'code': 3, 'description': 'Pago'}
```

### subscription.coupon

The **coupon** module performs the following operations:

- coupon.create(json)
- coupon.apply(subscription_code, coupon_code)
- coupon.fetch(coupon_code)
- coupon.fetch_all()
- coupon.set_status(coupon_code, status)
- coupon.remove(coupon_code)

```python
>>> from pyrecard.subscription import coupon
>>> response = coupon.set_status('coupon-0001', 'active')
>>> response
<Response [400]>
>>> response.json()
{'errors': [{'code': 'MA174', 'description': 'Coupon expirado.'}]}
```

More information check the [coupon documentation](https://dev.wirecard.com.br/v1.5/reference#coupons)


## Used by:

<img src="https://mexase.esp.br/static/images/logo/logo.png"
alt="Markdown Monster icon" width=160
style="float: left; margin-right: 10px;"  />
