from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return{"message : hello"}

# app.post("/api_v1/mlmodel")
def mlmodel(data:dict):

    return {}
