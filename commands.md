# Commands

## VENV

python -m venv venv

source venv/bin/activate

pip freeze > requirements.txt

pip install -r requirements.txt

## Terraform

terraform -chdir=terraform init

terraform -chdir=terraform plan

terraform -chdir=terraform apply

terraform -chdir=terraform destroy




# Local Database Creation

python scripts/local_db/local_db_connect.py

python scripts/local_db/local_db_create_db.py

python scripts/local_db/local_db_create_schema.py

python scripts/local_db/local_db_seed_data.py

python scripts/local_db/local_db_test_queries.py

python scripts/local_db/local_db_delete_db.py

python scripts/local_db/local_db_export_to_json.py



# Docker Database Creation

(On hold)


# AWS RDS Python Scripts

python scripts/aws_rds/aws_rds_connect.py

python scripts/aws_rds/aws_rds_schema_creation_and_testing.py

python scripts/aws_rds/aws_rds_schema_deletion_and_testing.py




# Create CIDR

python scripts/utils/create_cidr.py

