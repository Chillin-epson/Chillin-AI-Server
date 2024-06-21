from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import FileResponse
from pathlib import Path

from examples.convert_to_GIF import convert_to_GIF
from services.img_to_np import img_to_np

motion =  APIRouter()

@motion.post("/")
async def get_drawing_with_motion(
    image: UploadFile = File(...),
    motion: str = Form(...)
):
    img = await img_to_np(image)

    convert_to_GIF(img=img, char_anno_dir="output", motion_type=motion)

    gif_path = Path("output/video.gif")
    
    if not gif_path.is_file():
        return {"error": "gif not found"}
    return FileResponse(gif_path)
