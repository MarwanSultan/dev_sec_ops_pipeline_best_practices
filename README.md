# DevSecOps Pipeline Containerized Test Framework

This repository demonstrates a simple and effective DevSecOps pipeline that integrates security into every stage of the CI/CD process.

## Overview

This project showcases how to:

- Build a CI/CD pipeline using GitHub Actions
- Integrate security testing tools (e.g., SAST, dependency scanning)
- Use Docker to create consistent test environments
- Apply security best practices throughout development and deployment

## Project Structure


## Tools Used

- **GitHub Actions** — CI/CD automation
- **Docker** — containerized testing environment
- **Bandit** (Python SAST) / **Trivy** (container scanning)

## How to Run

To build and test locally using Docker:

```bash
docker build -t devsecops-app .
docker run --rm devsecops-app


# Grafana Dashboards

This project provides a **ready-to-run Grafana setup** for the Bank mock banking database. It includes preconfigured dashboards and a data source so you can **visualize your banking data immediately** using Docker Compose — no manual imports required.

The goal is to make it easy for QA engineers, developers, or anyone experimenting with the database to **monitor transactions, balances, and other metrics** in real time.

---

## Features

- Automatic provisioning of Grafana dashboards from JSON files  
- Automatic provisioning of Prometheus (or other) datasources  
- Docker Compose setup for one-command startup  
- Sample dashboards for account activity, transactions, and balances  

---

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed  
- The Bank database running (or compatible backend for metrics)  

---

### Setup & Run

1. Clone the repo:

```bash
git clone https://github.com/MarwanSultan/dev_sec_ops_pipeline_containerized_test_framework.git
cd dev_sec_ops_pipeline_containerized_test_framework

### Build the docker image
docker-compose up -d

### Open Grafana in your browswer
http://localhost:3000

### Credentials
Username: admin
Password: admin

### Build dashboards for data visualization