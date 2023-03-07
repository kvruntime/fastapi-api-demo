from fastapi_offline import FastAPIOffline

app = FastAPIOffline()


@app.get("/")
def index() -> str:
    return "Hello Guys"
