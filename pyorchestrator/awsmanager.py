import boto3
import botocore.exceptions
import click


def create_instance(params: dict) -> str:
    try:
        ec2 = boto3.client("ec2")

        instance_params = {
            "ImageId": params["ami"],
            "InstanceType": params["instance_type"],
            "SubnetId": params["subnet_id"],
            "SecurityGroupIds": params["security_group_ids"],
            "MinCount": 1,
            "MaxCount": 1,
        }

        if "key_name" in params and params["key_name"]:
            instance_params["KeyName"] = params["key_name"]

        instance = ec2.run_instances(**instance_params)

        return instance["Instances"][0]["InstanceId"]
    except botocore.exceptions.NoCredentialsError:
        click.echo("Error: No valid AWS credentials found.")
        exit(1)
    except botocore.exceptions.PartialCredentialsError:
        click.echo("Error: Partial AWS credentials found.")
        exit(1)
    except botocore.exceptions.EndpointConnectionError as e:
        click.echo(f"Error: Could not connect to the endpoint. {e}")
        exit(1)
    except botocore.exceptions.ClientError as e:
        click.echo(f"Client error: {e}")
        exit(1)
    except Exception as e:
        click.echo(f"An unexpected error occurred: {e}")
        exit(1)


def delete_instances(instance_ids: list[str]):
    """
    Terminates the specified or a list of EC2 instances.

    Args:
        instance_ids (list[str]): A list of instance IDs to terminate.
    Returns:
        None
    """

    try:
        ec2 = boto3.client("ec2")
        ec2.terminate_instances(InstanceIds=instance_ids)
    except botocore.exceptions.NoCredentialsError:
        click.echo("Error: No valid AWS credentials found.")
        exit(1)
    except botocore.exceptions.PartialCredentialsError:
        click.echo("Error: Partial AWS credentials found.")
        exit(1)
    except botocore.exceptions.EndpointConnectionError as e:
        click.echo(f"Error: Could not connect to the endpoint. {e}")
        exit(1)
    except botocore.exceptions.ClientError as e:
        click.echo(f"Client error: {e}")
        exit(1)
    except Exception as e:
        click.echo(f"An unexpected error occurred: {e}")
        exit(1)
