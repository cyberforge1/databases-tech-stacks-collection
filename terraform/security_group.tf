# terraform/security_group.tf

resource "aws_security_group" "rds_sg" {
  name        = "rds_security_group"
  description = "Allow all inbound and outbound traffic"
  vpc_id      = aws_vpc.main_vpc.id

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["163.47.68.73/32"] # Your public IP
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
