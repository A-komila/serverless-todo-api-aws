import json
import boto3
import logging
from boto3.dynamodb.conditions import Key


# Enable logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Connect to DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("TodoTable")



def get_user_id(event):
    """
    Extract authenticated user ID from Cognito
    """

    claims = event["requestContext"]["authorizer"]["claims"]

    return claims["sub"]



def lambda_handler(event, context):

    try:

        # Get authenticated user from Cognito
        user_id = get_user_id(event)


        # Get user's tasks
        response = table.query(

            KeyConditionExpression=
            Key("userId").eq(user_id)

        )


        tasks = response.get("Items", [])



        logger.info(

            "Tasks retrieved successfully for user %s",

            user_id

        )



        return {


            "statusCode": 200,


            "headers": {

                "Content-Type": "application/json"

            },


            "body": json.dumps({

                "tasks": tasks,

                "count": len(tasks)

            })

        }



    except Exception as e:


        logger.exception(

            "Error retrieving tasks"

        )


        return {


            "statusCode": 500,


            "headers": {

                "Content-Type": "application/json"

            },


            "body": json.dumps({

                "error": str(e)

            })

        }
