FROM ubuntu:16.04
LABEL REPO="https://github.com/mpmsimo/nsb"

# Upgrade the base OS
# Install dev, system, and debug tools
# Install packages for python
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git vim tar curl net-tools && \
    apt-get install -y python3.5 python3-pip python3.5-dev libffi-dev

# Create system directories
RUN mkdir -p /usr/bin/nsb/config
WORKDIR /usr/bin/nsb

# Copy requirements file and install requirements
COPY requirements.txt config/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r config/requirements.txt

# Copy Discord bot and API integrations
COPY nsb/nsb.py nsb.py
COPY nsb/logger.py logger.py
COPY scripts scripts
COPY nsb/api api

# Running discordbot locally
CMD ["python3", "nsb.py"]

# Label the the docker image with the GIT_HASH
ARG GIT_HASH
LABEL GIT_HASH=$GIT_HASH
ENV GIT_HASH=$GIT_HASH
