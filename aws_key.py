#!/usr/bin/env python
import json, re, sys, os, json
import subprocess
from subprocess import call, check_output
from lab_vars import set_lab_vars

#lab_vars='lab_vars.py'
#import lab_vars
def main(pod_number):
    name, region, az, csr_ami_id, csr_ami_id = set_lab_vars(pod_number)


    #1 - Create a Key Pair
    keypair_name=name
    print(keypair_name)
    region=region
    outfile_key_pair = 'keypair_name' + '.json'

    x = y

    #1 - Create a Key Pair
    #If it comes as .cer then you need to change it to .pem
    #openssl x509 -inform der -in cert.cer -outform pem -out cert.pem
    #aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text | out-file -encoding ascii -filepath MyKeyPair.pem
    cmd_keypair='aws ec2 create-key-pair --region' + " " + "{}".format(region) + " " + '--key-name' + " " + "{}".format(keypair_name) + " " + '--query \'KeyMaterial\' --output text >' + " " + "{}".format(keypair_name) + '.pem'
    output = check_output("{}".format(cmd_keypair), shell=True).decode().strip()
    print("Output: \n{}\n".format(output))

    with open(outfile_key_pair, 'w') as my_file:
        my_file.write(output)

    #Must run describe key pairs
    outfile_key_pair_id='key_pair_id.json'
    cmd_get_key_pair_id = 'aws ec2 describe-key-pairs' + " " + '--region' " " + "{}".format(region) + " " + '--key-names' + " " + "{}".format(keypair_name)

    output = check_output("{}".format(cmd_get_key_pair_id), shell=True).decode().strip()
    print("Output: \n{}\n".format(output))


    with open(outfile_key_pair_id, 'w') as my_file:
        my_file.write(output)

    outfile_key_pair_id='key_pair_id.json'
    with open (outfile_key_pair_id) as access_json:
        read_content = json.load(access_json)
        question_access=read_content['KeyPairs']
        question_data=question_access[0]
        replies_access=question_data['KeyPairId']
        keypairid=replies_access
        print(keypairid)

if __name__ == '__main__':
    main(sys.argv[1])