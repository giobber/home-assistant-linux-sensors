from pydantic import BaseModel, HttpUrl


class TemperatureDevice(BaseModel):
    device_name: str
    paths: list[HttpUrl]


class TemperatureSensor(BaseModel):
    name: str
    value: float
