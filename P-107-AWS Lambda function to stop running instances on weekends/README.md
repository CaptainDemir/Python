
# AWS Lambda Function: Stop Instances For Testing on Weekends

This AWS Lambda function is written in Python and designed to stop running instances in the test environment on weekends and start them on weekdays in the specified AWS region.

## Prerequisites

- AWS Account: You must have an AWS account to deploy and run this Lambda function.
- AWS CLI: Install and configure the AWS Command Line Interface (CLI) on your local machine.

## Deployment Steps

Follow the steps below to deploy the Lambda function:

1. Clone the repository or download the code files to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to create a deployment package:

   ```
   zip -r lambda_function.zip lambda_function.py
   ```

4. Sign in to your AWS Management Console.
5. Open the AWS Lambda service.
6. Click "Create function" and choose "Author from scratch".
7. Provide a name for your function, such as "StopStartInstancesOnWeekends".
8. Select "Python 3.8" as the runtime.
9. Under "Code entry type", select "Upload a .zip file" and click the "Upload" button.
10. Choose the `lambda_function.zip` file you created in step 3.
11. Set the "Handler" field to `lambda_function.lambda_handler`.
12. Under "Basic settings", increase the "Timeout" value if necessary (e.g., 5 minutes).
13. Configure the desired "Execution role" for the Lambda function or create a new role.
14. Click "Create function" to create the Lambda function.
15. Scroll down to the "Environment variables" section and add the following variable:

    - `REGION_NAME`: Replace with the desired AWS region name (e.g., us-west-2).

16. Save the changes.

## Usage

Once the Lambda function is deployed, you can manually trigger it or configure a schedule to automatically execute it.

To manually trigger the function:

1. Open the AWS Lambda service.
2. Select your function ("StopStartInstancesOnWeekends").
3. Click "Test" in the upper-right corner.
4. Create a new test event or choose an existing one.
5. Click "Test" to execute the function.

To configure a schedule:

1. Open the AWS CloudWatch service.
2. Click "Rules" in the left sidebar.
3. Click "Create rule".
4. Under "Event source", select "Schedule".
5. Configure the desired schedule expression (e.g., `cron(0 0 ? * MON-FRI *)` for weekdays).
6. Add the Lambda function as a target.
7. Click "Configure details" and provide a name and description for the rule.
8. Click "Create rule" to schedule the Lambda function.

## Customization

You can customize the Lambda function by modifying the following parts of the code:

- **REGION_NAME**: Replace with the desired AWS region where your instances are running.
- **Filter criteria**: Adjust the filters in the code to match your instance tagging scheme or other criteria.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The code in this project is adapted from the AWS SDK for Python (Boto3) documentation.

Feel free to update the README with additional information or sections as needed.