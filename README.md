# Simple Python Hello world web Application

## Deploy python sample application on our location workstation

Build the image using the following command

```bash
$ docker build --tag python-app  .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 python-app
```

The application will be accessible at http://localhost:5000/


## Deploy sample application to EC2 instance

pre req: created AMI with the following
- Local worksttion should has the python3 and boto module installed
- Insatlled git, python3
- Added my ssh key to e2c_user
- Opened port 80 to listen web application

Create EC2 instance
```bash
$ python3 create_ec2_instance.py <AWS_CREDENTIALS> (creds file should be in json format)
```
(script gives you the EC2 instance public ip)

Login to EC2 instance

```bash
$ ssh ec2-user@<ip>
```
Clone git repo to the EC2 instance.

```bash
$ git clone https://github.com/jogipraveen/python-sample-app.git
```

Go to the repo
```bash
cd python-sample-app
```

Install python web application on EC2 instance.
```bash
python3 install_app.py
```

The application accessible at
```bash
http://<EC2_public_IP>:80/
```
