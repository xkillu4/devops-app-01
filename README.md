# DevOps App 01

Aplicación web básica desarrollada con Flask y PostgreSQL, dockerizada con Docker y Docker Compose.

El objetivo del proyecto es practicar despliegue de aplicaciones, gestión de servicios, variables de entorno, persistencia de datos y health checks en un entorno containerizado.

## Tecnologías utilizadas

- Python
- Flask
- PostgreSQL
- Docker
- Docker Compose

## Arquitectura

El proyecto contiene dos servicios principales:

- `web`: aplicación Flask.
- `db`: base de datos PostgreSQL.

La aplicación se conecta a PostgreSQL usando variables de entorno definidas en el archivo `.env`.

## Estructura del proyecto

```text
.
├── app/
│   └── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

## Cómo ejecutar

```bash
docker-compose up --build
