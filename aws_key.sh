#!/bin/sh
export AWS_PAGER=""
rm -rf __pycache__
python3 aws_key.py $1
cat *.pem








