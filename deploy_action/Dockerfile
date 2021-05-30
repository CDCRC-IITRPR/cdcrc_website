FROM debian:buster-slim


RUN apt-get update

# installing dependencies
RUN apt-get install openconnect network-manager-openconnect openssh-client -y

# Copying entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
COPY remote_leader.sh /remote_leader.sh

RUN chmod +x remote_leader.sh
RUN chmod +x entrypoint.sh


ENTRYPOINT ["/entrypoint.sh"]
