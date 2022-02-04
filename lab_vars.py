def set_lab_vars(pod):
    name = "student" + pod
    pod = int(pod)
    region = None
    az = None
    csr_ami_id = None
    ubuntu_ami_id = None
    if (pod % 4 == 1) :
        region = 'us-west-1'
        az = 'us-west-1a'
        csr_ami_id = 'ami-0b6cee046d4cae9a9'
        ubuntu_ami_id = 'ami-0514b4bd87dba7384'
    elif (pod % 4) == 2:
        region = "us-east-1"
        az = "us-east-1a"
        ubuntu_ami_id = "ami-0b359b42108ad6fd2"  # us-east-1
        csr_ami_id = "ami-067c66abd840abc24"  # us-east-1
    elif (pod % 4) == 3:
        region='us-west-2'
        az = "us-west-2a"
        csr_ami_id = "ami-0453b3bb1d98a0102"  # us-west-2
        ubuntu_ami_id = "ami-0ed08ddf96d9628f3"  # us-west-2
    elif (pod % 4) == 0:
        region='us-east-2'
        az = "us-east-2a"
        csr_ami_id = "ami-0d43ca842a14ff342"  # us-east-2
        ubuntu_ami_id = "ami-093ab2ee72248accb"  # us-east-2
    print('name:', name)
    print('region:', region)
    print('az:', az)
    print('csr_ami_id:', csr_ami_id)
    print('ubuntu_ami_id:', ubuntu_ami_id)
    return name, region, az, csr_ami_id, ubuntu_ami_id
