#!/bin/bash

# Ensure that the following env variables are set
# VPN_SERVER_IP
# VPN_USERNAME
# VPN_PASSWORD
# VPN_SERVER_CERT
# AUTH_GROUP
# SSH_KEY
# REMOTE_IP
# REMOTE_USERNAME

# Logging in to the VPN Client
echo -e $VPN_PASSWORD |  openconnect $VPN_SERVER_IP \
-u $VPN_USERNAME \
--servercert $VPN_SERVER_CERT \
--authgroup $AUTH_GROUP \
--passwd-on-stdin \
-b

# Add ssh keys
# deleting if there exists
mkdir -p ~/.ssh/
rm -rf ~/.ssh/some_secret_file
touch ~/.ssh/some_secret_file
echo "$SSH_KEY" >> ~/.ssh/some_secret_file
chmod 400 ~/.ssh/some_secret_file

# Add ssh keys to agent
eval $(ssh-agent -s)
ssh-add ~/.ssh/some_secret_file


chmod +x remote_leader.sh

# waiting for 5 seconds
sleep 5

# ssh into the server
ssh -t -o StrictHostKeyChecking=no "$REMOTE_USERNAME@$REMOTE_IP" "/bin/bash -s " < remote_leader.sh

# TODO: Push the logs file
