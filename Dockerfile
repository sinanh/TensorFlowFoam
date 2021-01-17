FROM ubuntu:18.04
RUN  apt-get update \
  && apt-get install -y wget \
  && apt-get install -y software-properties-common \
  && rm -rf /var/lib/apt/lists/*

RUN sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -"
RUN add-apt-repository http://dl.openfoam.org/ubuntu

RUN  apt-get update \
  && apt-get install -y openfoam5 \
   && rm -rf /var/lib/apt/lists/*
