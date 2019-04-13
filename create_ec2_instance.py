#!/usr/local/bin/python3
import subprocess
import json
import time
import boto.ec2
import argparse


def getargs():
    parser = argparse.ArgumentParser(description='Read AWS credentials(json format')
    parser.add_argument('aws_json', help='AWS access and secret key file location')
    args = parser.parse_args()
    return args


def main():
    args = getargs()
    json_file = open(args.aws_json)
    data = json.load(json_file)
    conn = boto.ec2.connect_to_region('us-east-2', aws_access_key_id=data['access_key_id'], aws_secret_access_key=data['secret_access_key'])
    create_instance = conn.run_instances('ami-0d8feb36111a09213', min_count=1,max_count=1,instance_type='t2.micro', key_name='ami-key',security_group_ids=['sg-0c2d9161ccec6ee4e'])
    print("EC2 instance id:" create_instance.instances[0])

    while create_instance.instances[0].update() != "running":
        time.sleep(5)  # Run this in a green thread, ideally

    print(create_instance.instances[0].ip_address)


if __name__ == '__main__':
    main()
