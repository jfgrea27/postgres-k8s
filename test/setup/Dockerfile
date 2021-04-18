FROM postgres:latest

ENV POSTGRES_DB BANK 
ENV POSTGRES_PASSWORD=mysecretpassword

COPY setup.sql /docker-entrypoint-initdb.d

COPY . /usr/src
