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
        new_status = body['status']

        # Update the status of the specified task
        response = table.update_item(
            Key={
                'userId': user_id,
                'taskId': task_id
            },
            UpdateExpression='SET #s = :new_status',
            ExpressionAttributeNames={
                '#s': 'status'
            },
            ExpressionAttributeValues={
                ':new_status': new_status
            },
            ReturnValues='ALL_NEW'
        )

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'message': 'Task updated successfully',
                'updatedTask': response['Attributes']
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }
