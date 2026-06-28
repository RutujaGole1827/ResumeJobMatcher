from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI(
    title="AI Resume Matcher API",
    description="Backend API for Resume-to-Job Matcher",
    version="1.0.0",
)


# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to AI Resume Matcher API"}


# Health check endpoint
@app.get("/health")
def health():
    return {"status": "Server is running successfully"}
