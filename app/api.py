import psutil
from fastapi import FastAPI
from fastapi.exceptions import HTTPException

api = FastAPI()


@api.get("/cpu")
def list_available_cpu_devices():
    return list(psutil.sensors_temperatures().keys())


@api.get("/cpu/{device}")
@api.get("/cpu/{device}/{core}")
def read_cpu_temperature(device, core: int = None):
    cpu_temp = psutil.sensors_temperatures()[device]
    if core is None:
        return cpu_temp

    if core < 0 or core >= len(cpu_temp):
        raise HTTPException(404, f"Core {core} not found (available: {len(cpu_temp)})")

    return cpu_temp[core]
