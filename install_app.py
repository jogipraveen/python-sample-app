#!/usr/local/bin/python3
import subprocess
import os

subprocess.run(['sudo', 'yum', 'update', '-y'])
subprocess.run(['sudo', 'yum', 'install', '-y', 'docker-18.06.1ce-8.amzn2'])
subprocess.run(['sudo', 'service', 'docker', 'start'])
subprocess.run(['sudo', 'systemctl', 'enable', 'docker'])
subprocess.run(['sudo', 'usermod', '-a', '-G', 'docker', 'ec2-user'])
subprocess.run(['sudo', 'docker', 'build', '--tag', 'python-app', '.', '--no-cache'])
subprocess.run(['sudo', 'docker', 'run', '-d', '-p', '80:5000', 'python-app'])
