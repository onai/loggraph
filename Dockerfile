FROM ubuntu:18.04

RUN apt update && apt install -y python3-pip git

RUN pip3 install pandas
WORKDIR /home/
RUN git clone https://github.com/onai/loggraph.git
WORKDIR /home/logtogiraph


ENTRYPOINT ["./run.sh"]
