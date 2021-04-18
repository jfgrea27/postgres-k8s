# Postgres Database Application

Disclaimer: This application is part of a MVP, Microservicers, Kurbenetes, PostgreSQL persistent storage and Redis caching storage Backend Project. IT was purposed as an exercise to help gain understanding of Microservices Architecture & Decisions, DevOps and more. 

This application handles HTTP requests from other Kurbenetes Components, fetching or upserting information on a PostgreSQL database that persists outside of the Kurbenetes cluster. 

## Design Decisions
An external PostgreSQL database was chosen since ensuring data consistency across Kurbenetes Components is not very suited to Kurbenetes' stateless Components.
Further, the data was mocked to be sensitive financial data and so, for the sake of this project, was deemed sensitive. Running PostgreSQL on Kurbenetes has the additional drawback that data may be erased if the cluster completely crashes. [Ref: (1)]  

## Requirements
TODO

## Networking 
The application is running from `minikube` and communicates to the external PostgreSQL. Additional configurations from the PostgreSQL side were needed in order to allow PostgreSQL to accept client requests from Kurbenetes. These were inspired by [Ref: (2)]


## Testing
Please refer to the `README.md` inside the `./test` directory of this repository for details on Testing. 

## TODO REMOVE THE FOLLOWING
```sh
docker build -t accounts-postgres-db .
docker run --name accounts-postgres-db-cont -it -p 5000:5000 accounts-postgres-db 
```




## References
(1) https://cloud.google.com/blog/products/databases/to-run-or-not-to-run-a-database-on-kubernetes-what-to-consider

(2) https://gist.github.com/MauricioMoraes/87d76577babd4e084cba70f63c04b07d
