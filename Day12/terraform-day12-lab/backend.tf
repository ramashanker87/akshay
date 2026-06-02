terraform {
  backend "s3" {
    bucket         = "akshay-day12-tf-state-20260602"
    key            = "day12/dev/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "akshay-day12-terraform-locks"
    encrypt        = true
    profile        = "devops"
  }
}