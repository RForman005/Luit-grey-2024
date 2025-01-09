import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instanceids= event.get('InstanceIds', [])

response = ec2.stop_instances(
   InstanceIds=['i-034e9f7acd86d5dbf', 'i-0d62f72f11e87e90d', 'i-0fe9e02e240aefc46'
   ],
)

print(response)  