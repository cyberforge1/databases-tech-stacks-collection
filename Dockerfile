# Use the official MySQL image
    FROM mysql:8.0

    # Set environment variables for MySQL
    ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD
    ENV MYSQL_DATABASE=tech_stack_collection_docker

    # Copy the schema and seed SQL files into the container
    COPY sql/setup_tech_stack_collection_docker.sql /docker-entrypoint-initdb.d/

    # Expose the MySQL port
    EXPOSE 3306