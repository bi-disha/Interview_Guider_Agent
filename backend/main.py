from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from backend.ibm_client import ask_agent
import uvicorn
import os

app = FastAPI()

class Query(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Server is running!"}

@app.get("/home")
def home():
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "index.html")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="index.html not found")
    return FileResponse(file_path)

@app.post("/api/generate")
def generate(query: Query):
    try:
        result = ask_agent(query.prompt)
        content = result["choices"][0]["message"]["content"]
        return {"response": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)



