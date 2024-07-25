FROM python:3.11-slim-buster

LABEL maintainer="nlp@thedeep.io"

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update -y && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock /code/

# Upgrade pip and install python packages for code
RUN pip install --upgrade --no-cache-dir pip poetry \
    && poetry --version \
    # Configure to use system instead of virtualenvs
    && poetry config virtualenvs.create false \
    && poetry install --no-root \
    # Remove installer
    && pip uninstall -y poetry virtualenv-clone virtualenv

COPY . /code/

EXPOSE 8501


ENTRYPOINT ["streamlit", "run", "hero.py", "--server.port=8501", "--server.address=0.0.0.0"]
