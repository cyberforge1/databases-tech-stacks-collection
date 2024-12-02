# scripts/docker/docker_db_create_db.py

import os
import subprocess
from dotenv import load_dotenv


def load_environment_variables():
    """Load environment variables from the .env file."""
    dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
    if not os.path.exists(dotenv_path):
        raise FileNotFoundError(f".env file not found at {dotenv_path}")
    load_dotenv(dotenv_path)


def create_dockerfile(db_name):
    """Create a Dockerfile for the MySQL database."""
    dockerfile_content = f"""
    # Use the official MySQL image
    FROM mysql:8.0

    # Set environment variables for MySQL
    ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD
    ENV MYSQL_DATABASE={db_name}

    # Copy the schema and seed SQL files into the container
    COPY sql/setup_{db_name}.sql /docker-entrypoint-initdb.d/

    # Expose the MySQL port
    EXPOSE 3306
    """

    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content.strip())
    print("Dockerfile created successfully.")


def build_docker_image(image_name):
    """Build the Docker image."""
    try:
        print("Building Docker image...")
        subprocess.run(["docker", "build", "-t", image_name, "."], check=True)
        print(f"Docker image '{image_name}' built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error building Docker image: {e}")
        exit(1)


def run_docker_container(container_name, image_name, db_root_password, db_port):
    """Run the Docker container."""
    try:
        print("Running Docker container...")
        subprocess.run([
            "docker", "run", "-d",
            "--name", container_name,
            "-p", f"{db_port}:3306",
            "-e", f"MYSQL_ROOT_PASSWORD={db_root_password}",
            image_name
        ], check=True)
        print(f"Docker container '{container_name}' started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Docker container: {e}")
        exit(1)


def main():
    """Main execution block."""
    try:
        # Load environment variables
        load_environment_variables()
        db_name = os.getenv("DOCKER_DB_NAME", "tech_stack_collection_docker")
        db_root_password = os.getenv("DOCKER_DB_ROOT_PASSWORD", "MyPass")
        db_port = os.getenv("DOCKER_DB_PORT", "3306")
        image_name = os.getenv("DOCKER_IMAGE_NAME", "mysql-tech-stack-docker")
        container_name = os.getenv("DOCKER_CONTAINER_NAME", "mysql-tech-stack-container")

        if not all([db_name, db_root_password, db_port, image_name, container_name]):
            raise ValueError("Missing required environment variables.")

        # Create Dockerfile
        create_dockerfile(db_name)

        # Build Docker image
        build_docker_image(image_name)

        # Run Docker container
        run_docker_container(container_name, image_name, db_root_password, db_port)

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
