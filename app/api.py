from fastapi import FastAPI

from . import sensors

api = FastAPI()
api.include_router(sensors.api)
