# client setup with credentials
# define region
# list cloudwatch log group (optional with filter for rentention)
# make decision
# make aws call to update the retention


import boto3

client = boto3.client('logs', region="us-east-1")


response = client.describe_log_groups(
    logGroupNamePrefix='*'
)

_temp_log_grou = []

for resource n response["logGroups"]:
	resource.retentionInDays > 7 
		__temp_log_grou.append(resource.arn)

for lg in _temp_log_grou:
	client.
