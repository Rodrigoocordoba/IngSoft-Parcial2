from fastapi import FastAPI

app = FastAPI()

var1="Hello Woarld"

@app.get("/")
async def root():
    return {"message": var1}