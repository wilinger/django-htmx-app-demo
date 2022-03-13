[![CI](https://github.com/wilinger/django-htmx-app-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/wilinger/django-htmx-app-demo/actions/workflows/ci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=wilinger_django-htmx-app-demo&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=wilinger_django-htmx-app-demo)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=wilinger_django-htmx-app-demo&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=wilinger_django-htmx-app-demo)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=wilinger_django-htmx-app-demo&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=wilinger_django-htmx-app-demo)

<!-- ABOUT THE PROJECT -->
# Django notecard app demo

A simple Django notecard app to demonstrate security considerations in a CICD workflow.

### Resources used
* Secrets management with [Doppler](https://www.doppler.com/)
* Simple Ajax requests without page refresh with [htmx](https://htmx.org/)
* Open source vulnerability scanning with [Snyk](https://snyk.io/)
* Private registry and image vulnerability scanning with [Harbor](https://goharbor.io)
* Code quality and SAST scan with [SonarCloud](https://sonarcloud.io/) to fix [security hotspots](https://github.com/wilinger/django-htmx-app-demo/pull/5)
* Detecting secrets via [pre-commit](https://pre-commit.com/) hook with [detect-secrets](https://github.com/Yelp/detect-secrets)
* Scanning secrets with [GitGuardian](https://www.gitguardian.com/) in CI

### Deployment examples
* [Docker-compose](docker-compose.yml) example
* Example deployment on Kubernetes utilizing sealed secrets to encrypt Kubernetes Secret token and Doppler to retrieve application secrets on [Kubernetes](https://github.com/wilinger/argocd-homelab/tree/main/kustomize/django-app)
* Live deployment utilizing Doppler/Heroku integration to deploy on [Heroku](https://django-htmx-app-demo.herokuapp.com/)

### Image vulnerability scanning with Harbor

Harbor is an open source registry that secures artifacts with policies and role-based access control, allows for images to be scanned for vulnerabilities, and signs images as trusted.  The screenshots below shows the results of the vulnerability scans of the base images `python:3.10.2-slim` with 109 vulnerabilities and  `python:3.10.2-alpine3.15` with zero vulnerabilities.

Using `python:3.10.2-slim` as base image  
<img width="508" alt="python3 10 2-slim" src="https://user-images.githubusercontent.com/17818801/158037280-dd2061f7-5ef0-470d-94e3-2a6d328849d3.png">

Using `python:3.10.2-alpine3.15` as base image  
<img width="533" alt="python3 10 2-alpine3 15" src="https://user-images.githubusercontent.com/17818801/158037558-08e47741-009f-46b5-8d0d-cdab42d5e392.png">

Note that this is just an example of Harbor's capabilities using Trivy as an image vulnerability scanner. Whether an image with or without vulnerabilities should be used in a production environment will depend on various factors such false positives, severity, risk acceptance threshold and mitigating controls in place.

### To do
* detailed write up of tools
* unit testing with pytest
