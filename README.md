# Simple Python Hello world web Application#

Build the image using the following command

```bash
$ docker build --tag python-app  .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 python-app
```

The application will be accessible at http://localhost:5000/


#Deploy sample application to EC2 instance
pre req: created AMI with insatlled git, python3 and added my ssh key to e2c_user(Opened port 80 to listen web application)
instance_type: t2.micro

```bash
$ python3 create_ec2_instance.py <AWS_CREDENTIALS> (creds file should be in json format)
```
gives you the EC2 public ip

```bash
$ git clone https://github.com/jogipraveen/python-sample-app.git
```
