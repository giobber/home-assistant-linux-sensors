import time

import typer

import app.sensors.cli

cli = typer.Typer()
cli.add_typer(app.sensors.cli.cli, name="sensors")


@cli.command()
def run(device: str, sensor: str, wait: int = 1):
    """Continuous read of temperatures"""
    import psutil

    while True:
        temperatures = psutil.sensors_temperatures()

        sensors: list
        if not (sensors := temperatures.get(device)):
            typer.echo("Device not found")
            return

        if sensor not in map(lambda s: s.label, sensors):
            typer.echo("Sensor not found")
            return

        typer.echo(next(s.current for s in sensors if s.label == sensor))

        time.sleep(wait)
