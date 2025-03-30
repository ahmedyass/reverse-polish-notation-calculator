from fastapi import FastAPI
from app.routes import calculator, export, history
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Calculatrice NPI",
    description="Une API REST pour calculer en notation polonaise inverse",
    version="25.3.0"
)

app.include_router(calculator.router, prefix="/api", tags=["Calculator"])
app.include_router(export.router, prefix="/api", tags=["Export"])
app.include_router(history.router, prefix="/api", tags=["History"])

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)