import boto3
import datetime

def lambda_handler(event, context):
    
    # Specify the AWS region
    region = 'us-east-1'  # Replace with your desired region code

    # Get the current day of the week
    current_day = datetime.datetime.now().strftime('%A')

    # Check if it's a weekend (Saturday or Sunday)
    if current_day == 'Saturday' or current_day == 'Sunday':
        # Create an EC2 client
        ec2_client = boto3.client('ec2')

        # Get all running instances with the 'Environment' tag set to 'Test'
        response = ec2_client.describe_instances(
            Filters=[
                {
                    'Name': 'tag:Environment',
                    'Values': ['Test']
                },
                {
                    'Name': 'instance-state-name',
                    'Values': ['running']
                }
            ]
        )

        # Stop each running instance
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                ec2_client.stop_instances(
                    InstanceIds=[instance_id]
                )

        print('Stopped instances on weekends')
    else:
        print('Not a weekend, skipping instance stop')

