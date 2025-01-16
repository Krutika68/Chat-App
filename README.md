# Frontend, Django Chat Application & AWS Lambda Functions

This repository contains a project that includes a responsive webpage with a fixed navbar and collapsible menu, a chat application built with Django, and AWS Lambda functions for basic operations.

## Project Overview

1. **Frontend Development**: A responsive webpage that features:
   - A fixed navbar.
   - Three sections: a left menu, main content area, and a right-side panel.
   - A collapsible left menu.
   - A footer at the bottom.
   - A JavaScript function to resize the page based on the screen width.

2. **Django Chat Application**:
   - Users can sign up and log in.
   - A collapsible left menu displaying all registered users.
   - Logged-in users can select others to start a chat.
   - Chat messages are stored in a database and displayed in the chat interface.
   - A WebSocket is used for real-time messaging.

3. **AWS Lambda Functions**:
   - A function that adds two numbers and returns the result.
   - A function that stores a document or PDF file in an AWS S3 bucket.

## Prerequisites

Ensure you have the following tools installed:
- **Python 3.x** (for Django backend)
- **Node.js** (for frontend and JavaScript functionality)
- **Django** (for the chat application backend)
- **AWS CLI** (for deploying Lambda functions)
- **AWS account** (for setting up Lambda and S3)

## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/Chat-App.git
cd WEB-PROJECT

### 2. Frontend Setup
1. Navigate to the frontend directory:
cd frontend

2. Install dependencies using npm:
npm install

3. Start the frontend development server:
npm start

4. Open the browser and go to http://localhost:3000 to view the frontend.

### 3. Django Setup
1. Navigate to the Django project directory:
cd chatapp

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows

3.Install required Python dependencies:
pip install -r requirements.txt

4. Run database migrations to set up the database:
python manage.py migrate

5. Create a superuser to access the Django admin panel:
python manage.py createsuperuser

6. Start the Django development server:
python manage.py runserver

7. Open the browser and go to http://localhost:8000 to access the Django backend.

### 4. AWS Lambda Functions Setup

1. Ensure AWS CLI is configured:

Run the following command and input your AWS credentials when prompted:
aws configure

2. Deploy the Lambda functions to AWS:

For the addition function:
- Create a file add_numbers.py containing the code for adding two numbers, then zip the file:
zip add_numbers.zip add_numbers.py
- Deploy the Lambda function:
aws lambda create-function --function-name addNumbers --runtime python3.8 --role arn:aws:iam::your-aws-account-id:role/your-lambda-role --handler add_numbers.lambda_handler --zip-file fileb://add_numbers.zip

For the S3 file upload function:
- Create a file store_file_in_s3.py containing the code to upload files to an S3 bucket, then zip the file:
zip store_file_in_s3.zip store_file_in_s3.py
- Deploy the Lambda function:
aws lambda create-function --function-name storeFileInS3 --runtime python3.8 --role arn:aws:iam::your-aws-account-id:role/your-lambda-role --handler store_file_in_s3.lambda_handler --zip-file fileb://store_file_in_s3.zip

3. Ensure the AWS S3 bucket exists to store the uploaded documents.

### 5. Running the Full Application
Now that both the frontend and backend are running, follow these steps:

1. Start the frontend by running npm start in the frontend directory.

2. Start the backend by running python manage.py runserver in the django_chat_app directory.

3. Open two browser tabs:

- One for the frontend: http://localhost:3000
- One for the backend (Django admin or chat app): http://localhost:8000

4. Sign up or log in to the chat application, and interact with the frontend and backend.
