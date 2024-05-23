import typer

from . import handlers

cli = typer.Typer()


@cli.command()
def list_devices():
    for device in handlers.list_devices():
        typer.echo(device)


@cli.command()
def list_sensors(device: str = None):
    if device is not None:
        for sensor in handlers.list_sensors(device):
            typer.echo(sensor)
    else:
        for device in handlers.list_devices():
            typer.echo(f"{device}:")
            for sensor in handlers.list_sensors(device):
                typer.echo(f"\t{sensor}")
            typer.echo()


@cli.command()
def read(device: str, sensor: str):
    typer.echo(f"{handlers.read_temperature(device, sensor):.2f} °C")
