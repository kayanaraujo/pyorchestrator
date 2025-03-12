from fastapi import APIRouter
from ..app import awsmanager


router = APIRouter(prefix="/aws")


@router.get("/ec2")
def list_vms():
    return {"instances": awsmanager.list_instances()}


@router.post("/ec2")
def create_vm(params: dict):
    return {"instance_id": awsmanager.create_instance(params)}


@router.delete("/ec2/{instance_id}")
def delete_vm(instance_id: str):
    awsmanager.delete_instances([instance_id])
    return {"message": f"Instance {instance_id} deleted!"}
