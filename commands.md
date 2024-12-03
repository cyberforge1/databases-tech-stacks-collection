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


# Docker Database Creation

(On hold)


# AWS RDS Creation


# Create CIDR

python scripts/utils/create_cidr.py