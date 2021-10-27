from fastapi import APIRouter, File, UploadFile, HTTPException, status
from fastapi.responses import FileResponse
import shutil



router = APIRouter(prefix="/files", tags=["File"])


@router.post("/file")
def get_file(file: bytes = File(...)):
    content = file.decode("utf-8")
    lines = content.split('\n')
    return {"lines": lines}


@router.post("/upload")
def upload_file(file: UploadFile=File(...)):
    path = f"media/{file.filename}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        "filename": path,
        "type": file.content_type
    }


@router.get("/download/{name}", response_class=FileResponse)
def download_file(name: str):
    path = f"media/{name}"
    return path
