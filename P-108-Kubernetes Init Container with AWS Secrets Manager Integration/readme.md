# Kubernetes Init Container with AWS Secrets Manager Integration

This repository provides an example Python script that can be used as an init container in Kubernetes to fetch secrets from AWS Secrets Manager. This approach helps to securely retrieve sensitive information, such as database credentials, at runtime without hard-coding them in your application code or configuration files.

## Use case
You have a Kubernetes application that requires access to a database, and you want to securely store the database credentials in AWS Secrets Manager. Instead of hard-coding the credentials in your application code or configuration files, you can use an init container to fetch the credentials from AWS Secrets Manager at runtime.



## Prerequisites

- AWS account with appropriate permissions to access AWS Secrets Manager.
- Docker installed on your local machine to build and publish the container image.
- Kubernetes cluster where you can deploy the Kubernetes Pod.

## Usage

Follow the steps below to deploy the Python script as an init container in Kubernetes:

1. Store the Secrets in AWS Secrets Manager:
   - Create a secret in AWS Secrets Manager to store the required secrets, such as database credentials. Make a note of the secret name.

2. Build and Publish the Init Container Image:
   - Modify the `Dockerfile` provided in this repository as per your requirements.
   - Build the container image using Docker and publish it to a container registry accessible to your Kubernetes cluster.

3. Define the Kubernetes Pod Specification:
   - Create a YAML file (e.g., `pod.yaml`) to define the Pod specification.
   - Configure the `pod.yaml` file to include the main container for your application and an init container.
   - Specify the image name of the init container as the image you built and published in the previous step.
   - Set the `SECRET_NAME` environment variable in the init container to the name of the secret stored in AWS Secrets Manager.

4. Deploy the Kubernetes Pod:
   - Apply the `pod.yaml` file to your Kubernetes cluster using the `kubectl apply` command.
   - Kubernetes will create the Pod with the main container and the init container.
   - The init container will fetch the secret value from AWS Secrets Manager and make it available for the main container.

5. Access the Secret Value in your Application:
   - In your application code, access the secret value from the shared volume or environment variable set by the init container.
   - Use the secret value to establish secure connections or perform other required actions.


## Note
docker build -t your-registry/your-image-name .
docker push your-registry/your-image-name
kubectl apply -f database_deploy.yaml



## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## Resources

- [AWS Secrets Manager Documentation](https://aws.amazon.com/secrets-manager/)
- [Kubernetes Documentation](https://kubernetes.io/)

