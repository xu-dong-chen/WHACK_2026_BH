from fastapi import FastAPI

app = FastAPI()

@app.get("/top-win-rates")
def getTopWinRates():
    #results = call some function
    return {"results": results}