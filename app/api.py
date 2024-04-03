from fastapi import Depends, FastAPI

from . import auth, sensors

api = FastAPI()
api.include_router(sensors.api, dependencies=[Depends(auth.check_credentials)])
api.include_router(auth.api)
