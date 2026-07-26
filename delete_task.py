import json
import boto3
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


        # Get task ID
        task_id = body.get("taskId")


        # Validate input
        if not task_id:

            return {

                "statusCode": 400,

                "headers": {

                    "Content-Type": "application/json"

                },

                "body": json.dumps({

                    "error": "taskId is required"

                })

            }



        # Delete task
        table.delete_item(

            Key={

                "userId": user_id,

                "taskId": task_id

            }

        )



        logger.info(

            "Task deleted successfully for user %s",

            user_id

        )



        return {


            "statusCode": 200,


            "headers": {

                "Content-Type": "application/json"

            },


            "body": json.dumps({

                "message": "Task deleted successfully"

            })

        }



    except Exception as e:


        logger.exception(

            "Error deleting task"

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
