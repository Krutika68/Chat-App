def lambda_handler(event, context):
    # Extract numbers from the event (input payload)
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)
    
    # Perform the addition
    result = num1 + num2
    
    return {
        'statusCode': 200,
        'body': f"The result is: {result}"
    }
