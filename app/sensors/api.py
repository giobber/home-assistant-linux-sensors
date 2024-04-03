import psutil
from fastapi import APIRouter, Request

from .models import TemperatureDevice, TemperatureSensor

router = APIRouter()


@router.get("/temperature")
def list_available_cpu_devices(request: Request):
    sensors = [
        TemperatureDevice(
            device_name=device,
            paths=[f"{request.url}/{device}/{i}" for i, _ in enumerate(sub_devices)],
        )
        for device, sub_devices in psutil.sensors_temperatures().items()
    ]
    return sensors


@router.get("/temperature/{device}")
@router.get("/temperature/{device}/{sub_device}")
def read_cpu_temperature(device, sub_device: int = None):
    sensors = psutil.sensors_temperatures()[device]
    if sub_device is not None:
        sensor = sensors[sub_device]
        return TemperatureSensor(name=sensor[0], value=sensor[1])
    return [TemperatureSensor(name=sensor[0], value=sensor[1]) for sensor in sensors]
