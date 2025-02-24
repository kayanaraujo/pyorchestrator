import click
import botocore.exceptions
import pyorchestrator.awsmanager as awsmanager
from prettytable import PrettyTable


@click.group()
def vm():
    pass


@click.command()
@click.option("--name", type=str, help="The desired VM name")
@click.option("--size", type=str, help="The desired VM size")
@click.option("--image", type=str, help="The base image to create the VM")
@click.option(
    "--ssh-key", type=str, help="The SSH key-pair used to connect into the VM"
)
@click.option(
    "--provider",
    type=click.Choice(["aws"]),
    help="The cloud provider desired to create the resources.",
)
def create(name, size, image, ssh_key, provider):
    """Creates a virtual machine on Cloud"""

    error_tag = click.style("ERROR", bold=True, fg="red")

    try:

        params = {}

        if not name:
            raise ValueError(f"{error_tag}: A name must be informed")

        params["name"] = name

        if not size:
            raise ValueError(f"{error_tag}: You must set the hardware size")

        params["size"] = size

        if not image:
            raise ValueError(f"{error_tag}: The image must be defined")

        params["image"] = image
        params["ssh_key"] = ssh_key

        if not provider:
            raise ValueError(f"{error_tag}: The provider must be defined")

        if provider == "aws":
            vm_id = awsmanager.create_instance(params)
            click.echo(
                f"VM created with ID: {click.style(vm_id, bold=True, fg='green')}"
            )
    except (ValueError, botocore.exceptions.ClientError) as e:
        click.echo(e)
        exit(1)


@click.command()
@click.option("--id", type=str, help="The unique ID of the VM")
@click.option(
    "--provider", type=str, help="The provider where the VM should be deleted"
)
def delete(id, provider):
    """Deletes a virtual machine on Cloud"""

    try:
        if provider == "aws":
            awsmanager.delete_instances([id])

        click.echo(f"Deleted VM with ID: {click.style(id, bold=True)}")
    except (ValueError, botocore.exceptions.ClientError) as e:
        click.echo(e)
        exit(1)


@click.command()
@click.option(
    "--provider",
    type=str,
    help="The cloud provider where it will show the VMs",
)
def list(provider):
    """Lists all running/stopped VMs"""

    try:

        if not provider:
            raise click.BadParameter(f"You must inform a provider.")

        if provider == "aws":
            instances = awsmanager.list_instances()

        table = PrettyTable()

        if len(instances) > 0:
            table.field_names = ["ID", "Name", "Public IP", "State", "Region"]

            for instance in instances:
                vm_name = None

                for tag in instance["Tags"]:
                    if tag["Key"] == "Name":
                        vm_name = tag["Value"]
                        break

                table.add_row(
                    [
                        instance["InstanceId"],
                        vm_name,
                        instance["PublicIpAddress"],
                        instance["State"]["Name"],
                        instance["Placement"]["AvailabilityZone"],
                    ]
                )

            click.echo(table)
        else:
            click.echo("No active instances")
    except (
        ValueError,
        botocore.exceptions.ClientError,
        click.BadParameter,
    ) as e:
        click.echo(e)
        exit(1)


vm.add_command(create)
vm.add_command(delete)
vm.add_command(list)
