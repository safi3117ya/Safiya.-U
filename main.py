from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import router

app = FastAPI(
    title="LegalEase",
    description="AI Powered Legal Document Generator",
    version="1.0.0"
)

# Allow frontend (Streamlit) to connect with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.include_router(router, prefix="/api")


@app.get("/")
def home():
    return {
        "message": "LegalEase API is running!"
    }
