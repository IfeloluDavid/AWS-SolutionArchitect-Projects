import boto3
import os

# Initialize the SNS client
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # List of activities for the Solutions Architect role
    activities = [
        "Designing and implementing scalable, secure, and cost-effective cloud architectures.",
        "Conducting assessments of current cloud infrastructure and suggesting improvements.",
        "Collaborating with development teams to ensure applications are optimized for the cloud.",
        "Automating deployments and monitoring of cloud resources.",
        "Ensuring compliance with best practices for cloud security and cost management.",
        "Providing technical guidance and mentoring to team members.",
        "Writing and maintaining technical documentation for cloud solutions."
    ]
    
    # Format the activities into a message
    message = "Activities for Solutions Architect Role:\n\n" + "\n".join(f"- {activity}" for activity in activities)
    
    # Retrieve the SNS topic ARN from environment variables
    sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
    if not sns_topic_arn:
        return {
            'statusCode': 500,
            'body': "SNS_TOPIC_ARN environment variable is not set."
        }
    
    try:
        # Publish the message to the SNS topic
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject="Solutions Architect Activities"
        )
        return {
            'statusCode': 200,
            'body': f"Message sent to SNS topic: {response['MessageId']}"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error sending message: {str(e)}"
        }
