from schema import Schema, Or, Optional


common_schema = Schema(
    {
        "name": str,
        "provider": Or("aws", "azure"),
        "specs": dict,
    }
)

aws_schema = Schema(
    {
        "instance_type": str,
        "ami": str,
        Optional("key_name"): str,
        "security_group_ids": list,
        "subnet_id": str,
    }
)
