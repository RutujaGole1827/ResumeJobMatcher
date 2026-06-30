from fastapi import FastAPI
from app.routers import upload
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="AI Resume Matcher API", version="1.0.0")

# include router
app.include_router(upload.router, prefix="/api/resume")


@app.get("/")
def home():
    return {"message": "Welcome to AI Resume Matcher API"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # or ["*"] for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
