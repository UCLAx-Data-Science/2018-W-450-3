# Configure the AWS CLI

1. Create an Access Key
2. Install `pip` for Python 3

   ```
   sudo apt install python3-pip -y
   ```

3. Install the AWS CLI

   ```
   pip3 install awscli
   ```

4. Verify the version

   ```
   aws --version
   aws-cli/1.14.50 Python/3.5.2 Linux/4.4.0-1020-aws botocore/1.9.3
   ```

5. Configure the AWS CLI

   ```
   ubuntu@awsdriver:~$ aws configure
   AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
   AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   Default region name [None]: us-west-2
   Default output format [None]: table
   ```

6. Show the Instances Running on Your Account

   ```
   aws ec2 describe-instances
   ```
