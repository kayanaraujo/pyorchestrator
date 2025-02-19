import click
import pyorchestrator.command as command
from dotenv import load_dotenv


@click.group()
def cli():
    load_dotenv()


cli.add_command(command.vm)
