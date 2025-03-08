variable "region" {
    description = "The AWS region to deploy resources"
    default = "me-central-1"
}

variable "vpc_name" {
    description = "The name of the VPC"
    default = "my-vpc"
}

variable "vpc_cidr" {
    description = "The CIDR block for the VPC"
    default = "10.0.0.0/16"
}

variable "azs" {
    description = "A list of availability zones"
    default = ["me-central-1a", "me-central-1b", "me-central-1c"]
  
}

variable "public_subnet_cidrs" {
    description = "The CIDR block for the public subnet"
    default = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
    type = list(string)
}

variable "private_subnet_cidrs" {
    description = "The CIDR block for the public subnet"
    default = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
    type = list(string)
}

variable "tags" {
    description = "default tags to apply to all resources"
    default = {
        Terraform = "true"
        Environment = "dev"
    }
}
