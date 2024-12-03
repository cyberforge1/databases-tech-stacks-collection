# terraform/security_group.tf

resource "aws_security_group" "rds_sg" {
  name        = "rds_security_group"
  description = "Allow RDS access from my local machine"
  vpc_id      = aws_vpc.main_vpc.id

  ingress {
    description      = "Allow MySQL from local machine"
    from_port        = 3306
    to_port          = 3306
    protocol         = "tcp"
    cidr_blocks      = [var.LOCAL_CIDR]
  }

  egress {
    description      = "Allow all outbound traffic"
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "tech-stacks-collection-rds-sg"
  }
}

output "security_group_id" {
  value = aws_security_group.rds_sg.id
}
