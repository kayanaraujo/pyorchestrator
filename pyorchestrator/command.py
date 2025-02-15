import click
import pyorchestrator.reader as reader
import pyorchestrator.awsmanager as awsmanager


@click.group()
def vm():
    pass


@click.command()
@click.option(
    "-f",
    "--file",
    type=str,
    help="The YAML file that contains all the required attributes",
)
def create(file):
    """Creates a virtual machine on Cloud"""

    try:
        if not file:
            raise click.BadParameter(
                "You must inform a valid YAML file.", param_hint="--file"
            )

        yaml_file = reader.read_file(file)

        for vm in yaml_file:
            if vm["provider"] == "aws":
                vm_id = awsmanager.create_instance(vm["specs"])
                click.echo(f"VM created with ID: {vm_id}")

    except click.BadParameter as error:
        click.echo(error)


@click.command()
@click.option("--id", type=str, help="The unique ID of the VM")
@click.option(
    "--provider", type=str, help="The provider where the VM should be deleted"
)
def delete(id, provider):
    """Deletes a virtual machine on Cloud"""

    if provider == "aws":
        awsmanager.delete_instances([id])

    click.echo(f"Deleted VM with ID: {id}")


vm.add_command(create)
vm.add_command(delete)
