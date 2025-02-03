from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Cookbook Generator API is running!"}

@app.get("/generate-cookbook/")
def generate_cookbook():
    return {"status": "success", "cookbook": "Your AI-generated cookbook is ready!"}
