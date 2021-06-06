# Deploying a FastAPI Docker Compose application to Okteto

This is the source code of the application built during the first [community call](https://youtu.be/jgftQFzVCfU) to demonstrate how to deploy docker-compose applications on Okteto.

## Running remotely

Clone the repository:

```console
$ git clone https://github.com/okteto/python-docker-compose
$ cd python-docker-compose
```

Spin a development container:

```console
$ okteto up
```

 Start the application from your container:
 
```console
$ python main.py
```