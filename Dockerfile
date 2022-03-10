FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.12 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    VENV_PATH="/app/.venv"
    
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

WORKDIR /app

RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg netcat && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

COPY ./docker-entrypoint.sh ./pyproject.toml ./poetry.lock /app/

# install poetry without creating virtual environment
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction

# create django user & collectedstatic folder
RUN useradd -ms /bin/bash -d /app django && \
    usermod -a -G django django && \
    mkdir /app/collectedstatic

# copy files over to app directory and set owner as django
COPY ./src /app/

# change owner to django
RUN chown -R django:django /app

# swtich to django user
USER django

EXPOSE 8000
