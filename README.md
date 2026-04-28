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
├── .dockerignore
└── README.md
```

## Variables de entorno

Antes de ejecutar el proyecto, crea un archivo `.env` a partir de `.env.example`.

En Linux/macOS:

```bash
cp .env.example .env
```

En Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Ejemplo de `.env`:

```env
POSTGRES_HOST=db
POSTGRES_DB=mydb
POSTGRES_USER=user
POSTGRES_PASSWORD=password
```

El archivo `.env` no debe subirse al repositorio.

## Cómo ejecutar

Construir y levantar los contenedores:

```bash
docker-compose up --build
```

La aplicación estará disponible en:

```text
http://localhost:5000
```

## Endpoints

### Health check

```http
GET /health
```

### Obtener usuarios

```http
GET /users
```

### Crear usuario

```http
POST /users
```

Ejemplo:

```bash
curl -X POST http://localhost:5000/users \
-H "Content-Type: application/json" \
-d '{"name": "Ismael"}'
```

## Persistencia

PostgreSQL utiliza un volumen Docker llamado `db_data` para conservar los datos aunque los contenedores sean recreados.

## Buenas prácticas aplicadas

- Imagen ligera `python:3.11-slim`.
- Ejecución con usuario no-root.
- Variables de entorno mediante `.env`.
- Plantilla pública `.env.example`.
- Exclusión de `.env` mediante `.gitignore`.
- Persistencia con volúmenes Docker.
- Separación de endpoints GET y POST.
- Endpoint `/health` para comprobación del servicio.
- Healthchecks en Docker Compose.
- Retry al iniciar la app para esperar a PostgreSQL.

## Objetivo

Este proyecto sirve como laboratorio práctico para reforzar conocimientos de despliegue, troubleshooting y operación de aplicaciones en entornos containerizados.
