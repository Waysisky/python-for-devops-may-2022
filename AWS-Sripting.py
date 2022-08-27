import boto3

ec2= boto3.resource('ec2')

instance= ec2.create_instances(
    ImagId="ami-020ef1e2f6c2cc6d6",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro")
print(instance[0].id)
