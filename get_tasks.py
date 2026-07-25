import json
import boto3
from boto3.dynamodb.conditions import Key

# Connect to the DynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def lambda_handler(event, context):
    try:
        # Read userId from the query string, e.g. /tasks?userId=user1
        user_id = event['queryStringParameters']['userId']

        # Fetch all tasks belonging to this user
        response = table.query(
            KeyConditionExpression=Key('userId').eq(user_id)
        )

        tasks = response['Items']

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'tasks': tasks,
                'count': len(tasks)
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }
