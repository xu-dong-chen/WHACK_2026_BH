from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil

app = FastAPI()

# origins = [
#     "http://localhost:5173/",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/top-win-rates")
def getTopWinRates():
    #results = call some function
    return {"results": 0}

UPLOAD_DIR = Path("backend/dataset")
UPLOAD_DIR.mkdir(exist_ok = True)

@app.post("/upload-file")
async def uploadFile(file: UploadFile):

    file_path = UPLOAD_DIR / "dataset.pgn"

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
