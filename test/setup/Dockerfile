FROM postgres:latest

ENV POSTGRES_DB bank 
ENV POSTGRES_PASSWORD=mysecretpassword

COPY setup.sql /docker-entrypoint-initdb.d

COPY . /usr/src
