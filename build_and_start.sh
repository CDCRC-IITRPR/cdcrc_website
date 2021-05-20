# This script includes commands to build and start the containers in detach mode

docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up -d
