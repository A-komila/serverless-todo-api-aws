# Serverless Todo API on AWS

A fully serverless REST API for a Todo application built using AWS
managed services.

## Architecture

User -\> Cognito User Pool -\> JWT Token -\> API Gateway REST API -\>
Cognito Authorizer -\> Lambda -\> DynamoDB

## AWS Services Used

  Service                Purpose
  ---------------------- -------------------------------
  Amazon Cognito         Authentication and JWT tokens
  API Gateway REST API   Secure API endpoint
  AWS Lambda             CRUD operations
  Amazon DynamoDB        Task storage
  IAM                    Permissions

## DynamoDB

Table:

`TodoTable`

Keys:

-   `userId` (String)
-   `taskId` (String)

Attributes:

-   `title`
-   `status`

## API Routes

Base URL:

`https://fjaqaujb49.execute-api.us-east-1.amazonaws.com/prod`

### POST /tasks

Create a task.

Body:

``` json
{
  "title": "Learn AWS Serverless"
}
```

### GET /tasks

Get authenticated user's tasks.

### PUT /tasks

Update task status.

Body:

``` json
{
  "taskId": "uuid",
  "status": "completed"
}
```

### DELETE /tasks

Delete a task.

Body:

``` json
{
  "taskId": "uuid"
}
```

## Lambda Functions

-   create_task.py
-   get_tasks.py
-   update_task.py
-   delete_task.py

All functions use Cognito JWT claims to identify users and do not trust
userId from clients.

## Security

-   Cognito User Pool authentication
-   API Gateway Cognito Authorizer
-   JWT authorization
-   User isolation using Cognito sub

## Testing Results

-   Create Task: Passed
-   Get Tasks: Passed
-   Update Task: Passed
-   Delete Task: Passed

## AWS Region

`us-east-1`

## Author

Ameen Komila
