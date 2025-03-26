terraform {
  providers {
     aws = {
        version = "> 5.0"
     }
 backend local {}
}

provider aws {
  region = "me-central-1"
}

module "ec2_instance" {

src = "terraform-provider-aws"
version =

}
