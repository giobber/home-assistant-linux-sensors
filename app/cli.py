import typer

import app.sensors.cli

cli = typer.Typer()
cli.add_typer(app.sensors.cli.cli, name="sensors")
