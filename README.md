# Notify

![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
![Celery Version](https://img.shields.io/badge/Celery-5.3.6-green)
![Docker](https://img.shields.io/badge/Docker-24.0-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1.28-blue?logo=kubernetes)

A notification scheduling app, letting users schedule self notifications.
Currently supports email notifications.

Built using Django Rest Framework and Celery.

### Project structure
The project consists of a backend django app (Api) and a celery worker (worker) connected through a
redis queue.

### Build
To run the project locally, make sure Docker and Docker Compose are installed on your system.
Then navigate to `api` directory and run `docker compose -f docker/local.yaml up`.

If you want to build each app independently, follow the following instructions:<br>
1. Api <br>
Navigate to the `api` directory and run `docker build -t api -f docker/Dockerfile .`.
2. Worker <br>
Navigate to the `worker` directory and run `docker build -t worker -f docker/Dockerfile .`.

Once both images are built, the app can be deployed on a K8s cluster by running the following commands:
1. `kubectl apply -f api/infrastructure/deployment.yaml`
2. `kubectl apply -f worker/infrastructure/configmap.yaml`
3. `kubectl apply -f worker/infrastructure/deployment.yaml`