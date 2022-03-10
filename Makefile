ifdef DJANGO_ENV
DJANGO_ENV := $(DJANGO_ENV)
else
DJANGO_ENV := dev
endif

THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: help build up start down destroy stop restart logs ps

help:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

.DEFAULT_GOAL := help

build:
		docker-compose -f docker-compose.yml build $(c)
up:
		doppler run -c dev -p django-htmx-app-demo -- docker-compose -f docker-compose.yml up -d $(c)
start:
		doppler run -- docker-compose -f docker-compose.yml start $(c)
down:
		docker-compose -f docker-compose.yml down $(c)
destroy:
		docker-compose -f docker-compose.yml down -v $(c)
stop:
		docker-compose -f docker-compose.yml stop $(c)
restart:
		docker-compose -f docker-compose.yml stop $(c)
		doppler run -- docker-compose -f docker-compose.yml up -d $(c)
logs:
		docker-compose -f docker-compose.yml logs --tail=100 -f $(c)
ps:
		docker-compose -f docker-compose.yml ps
req:
		poetry export --without-hashes -f requirements.txt --output requirements.txt