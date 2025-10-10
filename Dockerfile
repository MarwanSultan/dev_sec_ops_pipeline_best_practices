# Use slim Python base image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /dev_sec_ops_pipeline_containerized_test_framework

COPY . /dev_sec_ops_pipeline_containerized_test_framework

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port where metrics will be served
EXPOSE 8000

# Run pytest with junit xml output, then start metrics exporter
CMD pytest --junitxml=results.xml --tb=short --disable-warnings && python metrics_exporter.py
