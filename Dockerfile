FROM apache/airflow:2.10.1

COPY requirements.txt .

USER root
RUN apt-get update

USER airflow
RUN pip install -r requirements.txt

