# Postgres Database Application

This application handles request to Postgres database.

The application runs in Docker and is build inside the root folder by

```sh
docker build -t accounts-postgres-db .
docker run --name accounts-postgres-db-cont -it -p 5000:5000 accounts-postgres-db 
```

If you are getting issues with accessing your localhost Postgres from inside the container, please refer to this useful gist:

https://gist.github.com/MauricioMoraes/87d76577babd4e084cba70f63c04b07d

Note: Credits to the creator.


