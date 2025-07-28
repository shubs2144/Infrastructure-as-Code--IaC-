# Setup and Configuration


- 1 pulumi new aws-python -y
# This command initializes a new Pulumi project using the AWS Python template, setting up the necessary files and directories.

- 2 python3 -m venv venv
# This command creates a virtual environment named `venv` to isolate project dependencies.

- 3 source venv/bin/activate
# This command activates the virtual environment, allowing you to install and manage Python packages specific to this project.

- 4 pip install -r requirements.txt
# This command installs the required Python packages specified in the `requirements.txt` file, which are necessary for the Pulumi project to function correctly.

- 5 pulumi config set aws:region us-west-2
# This command sets the AWS region for the Pulumi project to `us-west-2`,



-  pulumi up 
# This will create a new Pulumi project using the AWS Python template and deploy the resources defined in the project.

- 3 