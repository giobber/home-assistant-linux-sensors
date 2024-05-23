import psutil


def list_devices() -> list[str]:
    return list(psutil.sensors_temperatures().keys())


def list_sensors(device: str) -> list[str]:
    return [sensor.label for sensor in psutil.sensors_temperatures().get(device, [])]


def read_temperature(device: str, label: str):
    sensors = psutil.sensors_temperatures().get(device, [])
    sensors = {s.label: s.current for s in sensors}
    return sensors.get(label, None)
