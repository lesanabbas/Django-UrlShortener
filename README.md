# Bytelink

## Overview
ByteLink is a robust and secure social networking application API developed using Django Rest Framework. Designed to cater to modern social interaction needs, ByteLink provides an extensive range of functionalities to facilitate seamless user engagement and interaction.

### Prerequisites
- Python 3.8 or higher
- Docker and Docker Compose
- PostgreSQL (for local development or You can also use [Railway](https://railway.app/)

## Installation Step (Docker Hub)

To get started, pull the Docker image from Docker Hub:

```bash
docker pull lesanabbas/bytelink
```
Now, create a container using that image
```bash
docker run -p 8001:8001 \
  -e POSTGRES_NAME=<NAME> \
  -e POSTGRES_USER=<USER> \
  -e POSTGRES_PASSWORD=<PASSWORD> \
  lesanabbas/bytelink

```
