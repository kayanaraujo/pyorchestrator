import click
import pyorchestrator.command as command


@click.group()
def cli():
    pass


cli.add_command(command.vm)
