from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="Pdf Chat API")

app.include_router(router)