import boto3
import os

def fetch_secret(secret_name):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name='your-aws-region')
    response = client.get_secret_value(SecretId=secret_name)

    if 'SecretString' in response:
        return response['SecretString']
    else:
        return response['SecretBinary']

def main():
    secret_name = os.environ.get('SECRET_NAME')
    secret_value = fetch_secret(secret_name)
    
    # Use the secret value to establish a database connection or perform other actions
    print(f"Database credentials: {secret_value}")

if __name__ == '__main__':
    main()
