FROM ubuntu:latest


COPY . /usr/src

WORKDIR /usr/src

RUN apt-get update -y && \
    apt-get install python3 -y  && \
    apt install python3-pip -y && \
    python3 -m pip install -r requirements/prod.txt

EXPOSE 5000:5000
ENTRYPOINT [ "python3" ]
CMD [ "src/app.py" ]