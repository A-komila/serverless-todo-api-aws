# Serverless Todo API on AWS

A secure serverless Todo API built using AWS managed services.

The project implements a complete CRUD backend with authentication, authorization, and persistent storage.

---

## Architecture Diagram

<img src="aws-todo-architecture.png" alt="AWS Todo API Architecture Diagram" width="850"/>

---

## Project Overview

This project demonstrates how to build a serverless REST API using AWS services.

Users authenticate through Amazon Cognito and receive a JWT token.  
The token is validated by API Gateway before allowing access to protected API endpoints.

The request is then routed to AWS Lambda functions that perform CRUD operations on DynamoDB.

---

## AWS Region

```
us-east-1
```

---

## AWS Services Used

### Amazon Cognito
- User authentication
- User pool management
- JWT token generation
- Secure API access

### Amazon API Gateway
- REST API endpoints
- Cognito JWT authorization
- Request routing

### AWS Lambda

Four Lambda functions handle Todo operations:

| Function | Method | Endpoint | Description |
|---|---|---|---|
| CreateTask | POST | `/tasks` | Create a new task |
| GetTasks | GET | `/tasks` | Retrieve user tasks |
| UpdateTask | PUT | `/tasks` | Update task status |
| DeleteTask | DELETE | `/tasks` | Delete a task |

### Amazon DynamoDB

Database table:

```
TodoTable
```

Primary Key Design:

```
Partition Key: userId
Sort Key: taskId
```

Each user can only access their own tasks.

---

## Authentication Flow

1. User signs in using Amazon Cognito.
2. Cognito generates a JWT token.
3. Client sends API requests with the JWT token.
4. API Gateway validates the token.
5. Authorized requests are forwarded to Lambda.
6. Lambda reads or writes data in DynamoDB.

---

## API Endpoints

Base URL:

```
https://fjaqaujb49.execute-api.us-east-1.amazonaws.com/prod
```

All endpoints require:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## Create Task

```
POST /tasks
```

Request body:

```json
{
    "title": "Learn AWS Serverless"
}
```

---

## Get Tasks

```
GET /tasks
```

---

## Update Task

```
PUT /tasks
```

Request body:

```json
{
    "taskId": "task-id",
    "status": "completed"
}
```

---

## Delete Task

```
DELETE /tasks
```

Request body:

```json
{
    "taskId": "task-id"
}
```

---

## Lambda Functions

The project contains four Lambda functions:

```
create_task.py
get_tasks.py
update_task.py
delete_task.py
```

Each function:

- Extracts the user identity from Cognito JWT claims.
- Does not trust userId values sent by clients.
- Accesses only the authenticated user's tasks.

---

## Security

The project follows AWS security best practices:

- Cognito authentication required for all API methods.
- JWT token validation through API Gateway.
- User isolation using Cognito `sub`.
- IAM least privilege permissions.
- No public database access.

---

## Technologies

- Python
- AWS Lambda
- Amazon API Gateway
- Amazon Cognito
- Amazon DynamoDB
- AWS IAM
- AWS CloudShell

---

## Testing Results

The API was tested successfully using AWS CloudShell.

Tested operations:

| Operation | Result |
|---|---|
| User Authentication | ✅ Passed |
| Create Task | ✅ Passed |
| Get Tasks | ✅ Passed |
| Update Task | ✅ Passed |
| Delete Task | ✅ Passed |

---

## Project Structure

```
serverless-todo-api-aws/

├── create_task.py
├── get_tasks.py
├── update_task.py
├── delete_task.py
├── aws-todo-architecture.png
└── README.md
```

---

## Author

A-komila

Built with AWS Serverless Architecture.
