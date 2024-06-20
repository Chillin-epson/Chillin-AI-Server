
from fastapi import FastAPI
from routers.motion_router import motion

app = FastAPI()

app.include_router(motion, prefix="/motion")

    