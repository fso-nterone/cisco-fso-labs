#!/bin/sh
cd input
chmod 400 sconrod.pem
export AWS_PAGER=""
rm -rf __pycache__
python3 configure_csr.py
