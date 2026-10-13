from fastapi import FastAPI

app = FastAPI(
    title="My Portfolio API",
    description="Backend API for interactive developer portfolio",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "message":"API running successfully",
        "status":"online"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }