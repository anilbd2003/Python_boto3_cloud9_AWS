# Python_boto3_cloud9_AWS
Automate using AWS SDK for python (boto3), cloud9, python script. 

# AWS Cloud9:

It is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser. 
It includes a code editor, debugger, and terminal. Cloud9 comes with a terminal that includes sudo privileges to the managed Amazon
EC2 instance that is hosting your development environment and a preauthenticated AWS Command Line Interface.
Cloud9 has two types of development environments: 

•	 EC2 environments (cloud9 creates EC2 instance & manage lifecycle, auto set AWS CLI)  

•	SSH environments (use your own server, manually configure instance, manual AWS CLI set up)

pip (package manager)

pip is a package-management system written in Python and is used to install and manage software packages. Pip connects to an online 
repository of public packages, called the Python Package Index.

pip install some-package-name  
pip uninstall some-package-name  


Boto3

It is AWS Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon 
S3 and Amazon EC2. Boto3 is maintained and published by AWS.  After installing boto3, you set up credentials (in e.g. ~/.aws/credentials). 

 [default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET

Then, set up a default region (in e.g. ~/.aws/config):
[default]
region=us-east-1
For Cloud9, you don’t need to worry about credentials set up (it comes with preauthenticated AWS Command Line Interface) 


Steps: 

1)	Login to AWS management console.

2)	Open Cloud9 -------Create environment

3)	Open recently created environment in cloud9 IDE

4)	Cloud9 has terminal with AWS CLI auto-configure with logged in user credentials

5)	Run command in terminal to verify: aws s3 ls

6)	Install python
      a.	sudo apt install python3.8 {for ubuntu}
      b.	sudo amazon-linux-extras install python3.8 {for amazon linux 2}
      c.	python3.8 -V
      
7)	Install pip 
      a.	curl -o https://bootstrap.pypa.io/get-pip.py   OR
      a.	wget https://bootstrap.pypa.io/get-pip.py
      b.	python3.8 get-pip.py
      
8)	Install boto3 (AWS SDK for python)
      a.	sudo pip3 install boto3 
      
9)	Get source code in cloud9 environment 
      a.	git clone {GitHub URL}    OR
      b.	curl -sL https://s3.amazonaws.com/ddb-deep-dive/dynamodb.tar | tar -xv
      
10)	Go to the folder where source code present  
      a.	cd repository_directory_cloned
      
11)	Run python file using syntax {python3 filename.py}
      a.	Python3 create_table.py
      
12)	Check for resource creation/update/deletion in AWS management console
