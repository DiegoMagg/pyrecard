#!/bin/sh
clear
rm -rf .coverage
rm -rf htmlcov
coverage run tests.py
coverage html
