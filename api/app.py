# api/app.py
from streamlit import FastAPI
from pydantic import BaseModel
from io import BytesIO
import base64
from PIL import Image

from inference import generate

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_image(req: Prompt):
    image: Image.Image = generate(req.prompt)
    buf = BytesIO()
    image.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return {"image_base64": b64}
