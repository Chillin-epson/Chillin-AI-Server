from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import FileResponse
from pathlib import Path

from examples.convert_to_GIF import convert_to_GIF
import cv2
import numpy as np

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


@motion.post("/test")
async def get_multipart_file(
    image: UploadFile = File(...),
    motion: str = Form(...)
):
    # image_data = await image.read() 
    # nparr = np.frombuffer(image_data, np.uint8)  
    # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img = await img_to_np(image)

    convert_to_GIF(img=img, char_anno_dir="output")

    gif_path = Path("output/video.gif")

    if not gif_path.is_file():
        return {"error": "gif not found on the server"}
    return FileResponse(gif_path)
