# terraform/variables.tf

variable "AWS_REGION" {
  type        = string
  description = "The AWS region to deploy resources"
  default     = "us-east-1"
}

variable "AWS_REGION_AZ" {
  type        = string
  description = "The availability zone for the VPC"
  default     = "us-east-1a"
}

variable "AWS_ACCOUNT_ID" {
  type        = string
  description = "The AWS Account ID"
}

variable "DB_NAME" {
  type        = string
  description = "The name of the RDS database"
  default     = "tech_stacks_collection_aws_rds"
}

variable "DB_USERNAME" {
  type        = string
  description = "The master username for the RDS instance"
  default     = "admin"
}

variable "DB_PASSWORD" {
  type        = string
  description = "The master password for the RDS instance"
  sensitive   = true
}

variable "INSTANCE_CLASS" {
  type        = string
  description = "The instance class for the RDS instance"
  default     = "db.t3.micro"
}

variable "LOCAL_CIDR" {
  type        = string
  description = "Your local machine's CIDR block for accessing RDS"
  default     = "192.168.1.0/24" # Replace with your actual local network CIDR
}
