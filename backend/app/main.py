from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .database.database import init_db

from .routes import auth, tasks, projects


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Project Flow API",
    version="0.1.0",
    description="API desarrollada para funcionar como el backend del desarrollo Project Flow de davidom.",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # SvelteKit dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(projects.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Project Flow API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
