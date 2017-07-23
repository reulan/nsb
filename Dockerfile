FROM ubuntu:14.04
LABEL REPO="https://github.com/mpmsimo/nsb"

# Upgrade the base OS
RUN apt-get update && apt-get upgrade

# Install packages for python and debugging
RUN apt-get install -y git vim tar python python-pip python-dev

# Create system directories
RUN mkdir nsb
RUN mkdir config

# Copy Discord bot and API integrations
COPY nsb.py nsb/nsb.py
COPY api nsb/api
COPY scripts nsb/scripts

# Copy requirements file and install requirements
COPY requirements.txt config/requirements.txt
RUN pip install -r config/requirements.txt

WORKDIR nsb
CMD ["python", "nsb.py"]

# Label the the docker image with the GIT_HASH
ARG GIT_HASH
LABEL GIT_HASH=$GIT_HASH
ENV GIT_HASH=$GIT_HASH
