# Integration Test setup 

In order to simulate a test case closest to production, integration tests are used with the  help of Docker.
This document provides the reader with instructions to set up the containerized testing environment.

## Requirements
TODO

## Deployment
The following instructions set up of the testing environment:

```sh
cd ./test/setup
docker build -t accounts-db-test . # Builds from Dockerfile
docker run --name db-accounts-test-cont -it -p 5432:5432 accounts-db-test # Running Container
```

## Testing

To run the integration tests, run the following in the `venv` environment inside the `./test` folder:

```sh
python -m unittest test.integration_test
```

