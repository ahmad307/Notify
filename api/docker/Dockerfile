FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app


RUN apt update && apt install -y --no-install-recommends curl
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.7.1 python3 -

ENV PATH="/root/.local/bin:$PATH"
RUN poetry config virtualenvs.create false && poetry install

EXPOSE 8000

RUN python3 manage.py collectstatic --no-input

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-c", "api/gunicorn.py", "api.wsgi:application"]