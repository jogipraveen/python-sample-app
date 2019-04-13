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
