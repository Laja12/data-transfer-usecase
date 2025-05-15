terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.0.0"
    }
  }
}
provider "aws" {
  region = "us-east-1"
}

module "json_to_xml_lambda" {
  source        = "./lambda/lambda_transform"
  function_name = "json-to-xml-transformer"
}
