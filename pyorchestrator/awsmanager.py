import boto3
import random


def get_subnet_id(client) -> str:

    result = client.describe_subnets(DryRun=False)

    if len(result["Subnets"]) == 0:
        raise ValueError("No subnets found!")

    index = random.randint(0, len(result["Subnets"]))

    return result["Subnets"][index]["SubnetId"]


def create_instance(params: dict) -> str:
    """
    Creates a VM instance with given parameters
    """
    client = boto3.client("ec2")

    instance_params = {
        "ImageId": params["image"],
        "InstanceType": params["size"],
        "SubnetId": get_subnet_id(client),
        "MinCount": 1,
        "MaxCount": 1,
        "TagSpecifications": [
            {
                "ResourceType": "instance",
                "Tags": [{"Key": "Name", "Value": params["name"]}],
            }
        ],
    }

    if "key_name" in params and params["key_name"]:
        instance_params["KeyName"] = params["key_name"]

    instance = client.run_instances(**instance_params)

    return instance["Instances"][0]["InstanceId"]


def delete_instances(instance_ids: list[str]) -> None:
    """
    Terminates the specified or a list of EC2 instances.

    Args:
        instance_ids (list[str]): A list of instance IDs to terminate.
    Returns:
        None
    """

    ec2 = boto3.client("ec2")
    ec2.terminate_instances(InstanceIds=instance_ids)


def list_instances() -> list[dict]:
    """
    List EC2 instances with specific states.
    This function uses the boto3 library to connect to the AWS EC2 service and
    retrieve a list of instances that are in the "running", "pending", or "stopped" states.
    Returns:
        list[dict]: A list of dictionaries, each containing details of an EC2 instance.
    """

    client = boto3.client("ec2")

    instances = client.describe_instances(
        DryRun=False,
        Filters=[
            {
                "Name": "instance-state-name",
                "Values": ["running", "pending", "stopped"],
            }
        ],
    )

    if len(instances["Reservations"]) > 0:
        return instances["Reservations"][0]["Instances"]

    return []
