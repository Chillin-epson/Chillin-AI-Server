import numpy as np
import cv2

async def img_to_np(img: any):
    image_data = await img.read() 
    nparr = np.frombuffer(image_data, np.uint8)  
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    return img_np
