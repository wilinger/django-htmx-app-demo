[![CI](https://github.com/wilinger/django-htmx-app-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/wilinger/django-htmx-app-demo/actions/workflows/ci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=wilinger_django-htmx-app-demo&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=wilinger_django-htmx-app-demo)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=wilinger_django-htmx-app-demo&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=wilinger_django-htmx-app-demo)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=wilinger_django-htmx-app-demo&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=wilinger_django-htmx-app-demo)

<!-- ABOUT THE PROJECT -->
## Django notecard app

Just a simple Django notecard demo app

### Resources used
* Secrets management with [Doppler](https://www.doppler.com/)
* Simple Ajax requests without page refresh with [htmx](https://htmx.org/)
* Open source vulnerability scanning with [Snyk](https://snyk.io/)
* Image vulnerability scanning with [Harbor](https://goharbor.io/)
* Code quality and SAST scan with [SonarCloud](https://sonarcloud.io/) to fix [security hotspots](https://github.com/wilinger/django-htmx-app-demo/pull/5)
* Secrets scanning with [GitGuardian](https://www.gitguardian.com/)

### To do
* deploy on k8s and heroku
* use Harbor as private registry for vulnerability scanning
* unit testing with pytest
