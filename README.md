# fastapi-demo

## Description

this command-api is training on API with fastAPI

## Technology

- Pyhton
- FastAPI
- Tortoise-ORM
- Aerich

## aerich

```pwsh
aerich init -t path.DB_CONFIG

aerich --app app_name init-db

aerich migrate --name "initial"
```

## Visualisation

![image](./public/screenshot/api-screenshot.png)

## How run

```sh
docker-compose up -d api-db

python .
```
