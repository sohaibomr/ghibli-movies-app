"""main
"""
import uvicorn
from fastapi import FastAPI

from app.routes import v1
from app.services import collect_movies
from app.utils import common

app = FastAPI(on_startup=[common.start_up, collect_movies.get_movies_people],
              on_shutdown=[common.shut_down])
app.include_router(v1.V1, prefix="", tags=["v1"])


# Running of app.
if __name__ == "__main__":
    uvicorn.run(
        app=app, host="127.0.0.1",  log_level="info",
    )
