import json
import boto3
import uuid

# Connect to the DynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def lambda_handler(event, context):
    try:
        # Parse the incoming request body
        body = json.loads(event['body'])

        user_id = body['userId']
        title = body['title']

        # Generate a unique task ID
        task_id = str(uuid.uuid4())

        # Save the new task to DynamoDB
        table.put_item(
            Item={
                'userId': user_id,
                'taskId': task_id,
                'title': title,
                'status': 'pending'
            }
        )

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'message': 'Task created successfully',
                'taskId': task_id
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }
