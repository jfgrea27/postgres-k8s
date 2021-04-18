# Integration Test setup 

In order to simulate a test case closest to production, integration tests are used with the  help of Docker.
This document provides the reader with instructions to set up the containerized testing environment.

## Requirements
The following are the necessary instructions to run the integration tests:
### Python Environment:
To set up the Python environment, please run:
- `cd` into root directory of this repository
- Create a `virtualenv` with `Python3.8` installed.
- Run `pip install  -r requirements/dev.txt`
### Deployment
To set up the Docker testing environment, run: 
- `cd` into `./test/setup`
- Build Dockerfile with `docker build -t accounts-db-test . `
- Run Docker container with `docker run --name db-accounts-test-cont -it -p 5432:5432 accounts-db-test`

### Testing
Lastly to test, run:
- `cd` into `./test` folder.
- Run `python -m unittest test.integration_test`

