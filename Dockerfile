# syntax=docker/dockerfile:1
FROM ubuntu:20.04
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3 python3-pip nano && rm -rf /var/lib/apt/lists/*
COPY . /app
RUN pip3 install jupyterlab numpy pandas matplotlib seaborn scikit-llm
