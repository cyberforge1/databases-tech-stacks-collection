# terraform/rds.tf

provider "aws" {
  region = var.AWS_REGION
}

resource "aws_db_subnet_group" "main" {
  name       = "rds_subnet_group"
  subnet_ids = [
    aws_subnet.main_subnet.id,
    aws_subnet.secondary_subnet.id
  ]

  tags = {
    Name = "rds_subnet_group"
  }
}

resource "aws_db_instance" "rds_instance" {
  identifier              = "tech-stacks-collection-aws-rds"
  allocated_storage       = 20
  max_allocated_storage   = 20
  engine                  = "mysql"
  engine_version          = "8.0.32"
  instance_class          = var.INSTANCE_CLASS
  db_name                 = var.DB_NAME
  username                = var.DB_USERNAME
  password                = var.DB_PASSWORD
  publicly_accessible     = true
  skip_final_snapshot     = true
  deletion_protection     = false
  backup_retention_period = 0
  vpc_security_group_ids  = [aws_security_group.rds_sg.id]
  db_subnet_group_name    = aws_db_subnet_group.main.name

  tags = {
    Name = "tech-stacks-collection-rds"
  }
}

output "rds_endpoint" {
  value = aws_db_instance.rds_instance.endpoint
}

output "rds_username" {
  value = aws_db_instance.rds_instance.username
}
