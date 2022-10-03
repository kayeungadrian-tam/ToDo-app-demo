import boto3
from boto3.dynamodb.conditions import Key
import pandas as pd


dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-northeast-1",
    endpoint_url="http://dynamodb-local:8100",
    aws_access_key_id="ACCESS_ID",
    aws_secret_access_key="ACCESS_KEY",
)

dynamo_table = dynamodb.Table("Tasks")


def create_task(data: dict):
    dynamo_table.put_item(Item=data)


def get_all_tasks():
    table = dynamo_table.scan()
    # res_df = pd.DataFrame(table["Items"])
    res_df = table["Items"]
    return res_df


def get_task(task_id):
    res = dynamo_table.query(
        KeyConditionExpression=Key("task_id").eq(task_id),
    )
    return res["Items"]
