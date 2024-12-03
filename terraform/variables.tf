# terraform/variables.tf

variable "AWS_REGION" {
  type        = string
  description = "The AWS region to deploy resources"
  default     = "ap-southeast-2"
}

variable "AWS_REGION_AZ" {
  type        = string
  description = "The availability zone for the VPC"
  default     = "ap-southeast-2a"
}

variable "AWS_ACCOUNT_ID" {
  type        = string
  description = "The AWS Account ID"
}

variable "DB_NAME" {
  type        = string
  description = "The name of the RDS database"
}

variable "DB_USERNAME" {
  type        = string
  description = "The master username for the RDS instance"
}

variable "DB_PASSWORD" {
  type        = string
  description = "The master password for the RDS instance"
  sensitive   = true
}

variable "INSTANCE_CLASS" {
  type        = string
  description = "The instance class for the RDS instance"
}

variable "LOCAL_CIDR" {
  type        = string
  description = "Your local machine's CIDR block for accessing RDS"
}
