import yaml
import pyorchestrator.yaml_validation as yaml_validation


def read_file(file: str) -> list[dict]:
    """
    Reads a YAML file, validate and returns its contents as a list of dictionaries.

    Args:
        file (str): The path to the YAML file to be read.

    Returns:
        list[dict]: The contents of the YAML file as a list of dictionaries.
    """
    with open(file, "r") as file:
        yaml_file = yaml.safe_load(file)

        for item in yaml_file:
            yaml_validation.common_schema.validate(item)

            if item["provider"] == "aws":
                yaml_validation.aws_schema.validate(item["specs"])
            elif item["provider"] == "azure":
                pass

    return yaml_file
