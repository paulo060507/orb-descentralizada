from fastapi import FastAPI
from fastapi.responses import JSONResponse
import base64, cv2
from .camera import Camera
from .pipeline import quality_score

app = FastAPI(title="Orb Local API")
cam = Camera()

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/capture")
def capture():
    frame = cam.read()
    score = quality_score(frame)
    _, buf = cv2.imencode(".jpg", frame)
    b64 = base64.b64encode(buf).decode()
    return JSONResponse({"quality": score, "image_jpg_base64": b64})
