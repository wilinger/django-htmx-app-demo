FROM python:3.9

# set environment variables
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
    
# set path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

WORKDIR /app

# install packages
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl gnupg netcat && \
    curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | apt-key add - && \
    echo "deb https://packages.doppler.com/public/cli/deb/debian any-version main" | tee /etc/apt/sources.list.d/doppler-cli.list && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python && \
    apt-get update && \
    apt-get -y install doppler

# copy poetry files
COPY pyproject.toml poetry.lock /app/

# install as root
RUN poetry install --no-interaction

# create django user
RUN useradd -ms /bin/bash -d /app django && usermod -a -G django django && chown -R django:django $POETRY_HOME

# copy files over to app directory and set owner as django
COPY --chown=django:django . /app/

# swtich to django user
USER django

EXPOSE 8000