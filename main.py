from fastapi import FastAPI

app = FastAPI()

var1="Hello Worrld"

@app.get("/")
async def root():
    return {"message": var1}
