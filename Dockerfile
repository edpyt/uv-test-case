FROM python:3.12-slim-bookworm

ARG APP_NAME=app

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

ADD https://astral.sh/uv/0.3.3/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.cargo/bin/:$PATH"

WORKDIR /$APP_NAME
COPY . /$APP_NAME

RUN uv sync --frozen

ENV VIRTUAL_ENV=/$APP_NAME/.venv
ENV PATH="/$APP_NAME/.venv/bin:$PATH"

RUN pip freeze
