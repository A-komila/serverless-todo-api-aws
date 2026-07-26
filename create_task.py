import json
import boto3
import uuid
import logging


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


        # Parse request body
        body = json.loads(event["body"])


        # Get task title
        title = body.get("title")


        # Validate input
        if not title:

            return {

                "statusCode": 400,

                "headers": {
                    "Content-Type": "application/json"
                },

                "body": json.dumps({

                    "error": "Title is required"

                })

            }



        # Generate task ID
        task_id = str(uuid.uuid4())



        # Save task
        table.put_item(

            Item={

                "userId": user_id,

                "taskId": task_id,

                "title": title,

                "status": "pending"

            }

        )



        logger.info(

            "Task created successfully for user %s",

            user_id

        )



        return {


            "statusCode": 201,


            "headers": {

                "Content-Type": "application/json"

            },


            "body": json.dumps({

                "message": "Task created successfully",

                "taskId": task_id

            })

        }



    except Exception as e:


        logger.exception(

            "Error creating task"

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
