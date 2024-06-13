from fastapi import FastAPI

app = FastAPI()

var1="Hello World"

465475464476

@app.get("/")
async def root():
    if True:
        return {"message": var1}
    else:
        return {"message": var1}
