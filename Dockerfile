FROM python:3.7

RUN pip install -U pipenv
WORKDIR /opt/initial_project

COPY Pipfile* ./
RUN pipenv install --system --deploy

COPY . .
CMD gunicorn -c gunicorn.conf.py initial_project.wsgi
