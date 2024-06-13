from fastapi import FastAPI

app = FastAPI()

var1="Hello World"

465475464476

@app.get("/")
async def root():
    return {"message": var1}
