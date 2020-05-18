from fastapi import FastAPI

# Config
app = FastAPI()

# Routes
@app.post('/sessions/')
def sessions_store():
    pass
