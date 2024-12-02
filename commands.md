# Commands

## VENV

python -m venv venv

source venv/bin/activate

pip freeze > requirements.txt



# Local Database Creation

python scripts/local_db/local_db_connect.py

python scripts/local_db/local_db_create_db.py

python scripts/local_db/local_db_create_schema.py

python scripts/local_db/local_db_seed_data.py

python scripts/local_db/local_db_test_queries.py

python scripts/local_db/local_db_delete_db.py


# Docker Database Creation

python scripts/docker/docker_db_create_db.py


# AWS RDS Creation