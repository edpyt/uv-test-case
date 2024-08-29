FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

ADD uv.lock /app/uv.lock
ADD pyproject.toml /app/pyproject.toml

RUN uv sync --frozen --no-install-project 

ADD . /app

RUN uv sync --frozen

ENV PATH="/app/.venv/bin:$PATH"
