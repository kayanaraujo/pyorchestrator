# pyor - AWS Infrastructure Management CLI

`pyor` is a command-line interface (CLI) tool designed to simplify the management of AWS virtual machines (EC2 instances). It allows users to create, list, and delete EC2 instances directly from the terminal.

## Features
- 🚀 **Create EC2 instances** in AWS
- 📋 **List all running/stopped instances**
- 🗑️ **Delete EC2 instances**
- 🔗 **Direct interaction with AWS SDK (boto3)**
- 🛠️ **Easy-to-use and lightweight CLI**

## Prerequisites
- Python 3.8+
- AWS CLI configured with valid credentials
- `poetry` as the dependency manager

## Installation
```sh
# Clone the repository
git clone https://github.com/kayanaraujo/pyorchestrator.git
cd pyorchestrator

# Install dependencies using Poetry
poetry install
```

## Usage
### List all EC2 instances
```sh
poetry run pyor vm list --provider=aws
```
Displays all EC2 instances with details like ID, state, type, and public IP.

### Create a new EC2 instance
```sh
poetry run pyor vm create --name my-instance --type t2.micro --region us-east-1 --provider aws
```
Creates a new EC2 instance with the specified name and type.

### Delete an EC2 instance
```sh
poetry run pyor vm delete --id i-0123456789abcdef0 --provider aws
```
Deletes an EC2 instance using its instance ID.

## Configuration
Ensure your AWS credentials are configured properly using the AWS CLI:
```sh
aws configure
```
Or set environment variables:
```sh
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="us-east-1"
```

## Roadmap
- ✅ Create, list, and delete EC2 instances
- 🌐 Web UI for better visualization

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## Author
[Your Name](https://github.com/kayanaraujo)

