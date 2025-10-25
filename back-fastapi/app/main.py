from fastapi import FastAPI
from .models import count_table

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/count")
def get_count():
    current_count = count_table.get_count()
    return {"count": current_count}

@app.post("/count/increment")
def increment_count():
    new_count = count_table.increment_count()
    return {"count": new_count}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
