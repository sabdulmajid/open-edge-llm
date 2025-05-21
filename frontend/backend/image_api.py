from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    # Save or process image here
    return {"filename": file.filename, "size": len(contents)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
