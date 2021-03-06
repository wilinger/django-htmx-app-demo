FROM python:3.10.2-alpine3.15

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.13 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    VENV_PATH="/app/.venv" \
    USER=django \
    GROUP=django \
    UID=1001 \
    GID=1001

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

WORKDIR /app

RUN apk update \
    && apk add curl postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python

COPY ./docker-entrypoint.sh ./pyproject.toml ./poetry.lock /app/

# install poetry without creating virtual environment
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction

# create django user
RUN addgroup --gid $GID "$GROUP" \
    && adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "$GROUP" \
    --no-create-home \
    --uid "$UID" \
    "$USER"

# copy files over to app directory
COPY ./src /app/

# # change owner to django
RUN chown -R $USER:$GROUP /app

# swtich to django user
USER $USER
