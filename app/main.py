from fastapi import FastAPI

from app.api.routes import router

import  logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

app = FastAPI(title="Pdf Chat API")

app.include_router(router)