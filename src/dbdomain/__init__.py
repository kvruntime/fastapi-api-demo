host="localhost:5432"
TORTOISE_ORM_CONFIG:dict = {
"connections":{
    "dev-string-connection":f"postgres://postgres:postgres@localhost:5432/postgres"
},
"apps":{
    "commands-api":{
        "models":["dbdomain.models", "aerich.models"],
        "default_connection":"dev-string-connection"
    }
}
}
