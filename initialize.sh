#!/bin/bash

# Update
sudo apt-get update

# Install tree
sudo apt install tree

# Download and install docker
# Second line is to change permissions so that there is no need to run docker with sudo

curl -sSL https://get.docker.com/ | sh
sudo usermod -aG docker ubuntu

# Download and install docker-compose
sudo curl -L https://github.com/docker/compose/releases/download/1.15.0/docker-compose-`uname -s`-`uname -m` > docker-compose
sudo mv docker-compose /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Create directories
mkdir data
mkdir docker
mkdir docker/jupyter
mkdir docker/mongo
mkdir docker/postgres
mkdir docker/flask
mkdir docker/app
mkdir docker/app/templates
mkdir docker/app/static
mkdir docker/app/static/css
mkdir docker/app/static/js
mkdir docker/app/static/data
mkdir notebook
mkdir lib
mkdir models
mkdir scrapy
mkdir config

sudo reboot

# Not neccesary unless you ran mkdir as root
# sudo chown ubuntu -R data
# sudo chown ubuntu -R docker
# sudo chown ubuntu -R notebook
# sudo chown ubuntu -R lib
