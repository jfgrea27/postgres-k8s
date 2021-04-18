# Postgres Database Application

This application handles request to Postgres database.

The application runs in Docker and is build inside the root folder by

```sh
docker build -t accounts-postgres-db .
docker run --name accounts-postgres-db-cont -it -p 5555:5555 accounts-postgres-db 
```