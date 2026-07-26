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


        # Get task information
        task_id = body.get("taskId")
        new_status = body.get("status")


        # Validate input
        if not task_id or not new_status:

            return {

                "statusCode": 400,

                "headers": {
                    "Content-Type": "application/json"
                },

                "body": json.dumps({

                    "error": "taskId and status are required"

                })

            }



        # Update task
        response = table.update_item(

            Key={

                "userId": user_id,

                "taskId": task_id

            },


            UpdateExpression="SET #s = :new_status",


            ExpressionAttributeNames={

                "#s": "status"

            },


            ExpressionAttributeValues={

                ":new_status": new_status

            },


            ReturnValues="ALL_NEW"

        )



        logger.info(

            "Task updated successfully for user %s",

            user_id

        )



        return {


            "statusCode": 200,


            "headers": {

                "Content-Type": "application/json"

            },


            "body": json.dumps({

                "message": "Task updated successfully",

                "updatedTask": response["Attributes"]

            })

        }



    except Exception as e:


        logger.exception(

            "Error updating task"

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
