import json
import boto3

# Connect to the DynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def lambda_handler(event, context):
    try:
        # Parse the incoming request body
        body = json.loads(event['body'])

        user_id = body['userId']
        task_id = body['taskId']

        # Delete the specified task
        table.delete_item(
            Key={
                'userId': user_id,
                'taskId': task_id
            }
        )

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'message': 'Task deleted successfully'
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }
