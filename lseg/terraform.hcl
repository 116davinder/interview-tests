# providers
# backend

backend s3 {
 bucket = ""
 path = "/test1"  ===> /test2
}

backend local {}

# variables
# resources

array = []

test1 = {
 instance = test1
 instance1 = test2
}

ec2.tf

terraform "aws_ec2_instance" "test1" {
 
 for_each map{}

 ami = "ami-xxxx"
 tags = {
	Name = try(each.key, "")
        Example = each.value ? true_value:false
 }
}

# variables
1. variables.dev.tfvars 
instance_name = "test"

terraform plan/apply --var-file variables.dev.tfvars

state migration 

