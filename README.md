# fastapi-demo

## Description

this command-api is training on API with fastAPI

## Technology

- Pyhton
- FastAPI
- Tortoise-ORM
- Aerich


## Before run the application

Install requirements

```bash
  pip install -r requirements.txt
```

Generate prisma client

```bash
  prisma generate
```

Check & run migrations

```bash
    prisma migrate dev
    prisma db push
```




## How run

Ensure postgres database instance is avalaible and accessible.

```sh
  fastapi dev --host=0.0.0.0
```
