from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database import Base, engine
from src.routes.auth_routes import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="FastAPI JWT Auth", lifespan=lifespan)
app.include_router(auth_router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
