# script to be run on the server, to deploy the application

# Ensure that $ENV_PATH is set
# You may use the export command to do like this or update the .bashrc
# export ENV_PATH="/workspaces/cred/.env"

# Ensure that docker is installed


REPO_URL=https://github.com/CDCRC-IITRPR/cdcrc_website

set -e

# TODO: Add Logic to see if Commit ID Changed


echo "Cloning the repo"
# Remove the directory if it exist
rm -rf cdcrc_website
git clone https://github.com/vinx-2105/cdcrc_website


cd cdcrc_website
git checkout prod --

echo "Moving the env file from the \$ENV_PATH to current directory"
cp $ENV_PATH ./.env

sudo chmod +x startup.sh

# adding the command in nginx/Dockerfile.prod to use the ssl config
cat <<'EOT' >> nginx/Dockerfile.prod
COPY nginx_with_ssl.conf /etc/nginx/conf.d/nginx.conf
EOT



# Building 
echo "Build the application"
docker-compose -f docker-compose.prod.yml build --no-cache

echo "Start the application"
docker-compose -f docker-compose.prod.yml up -d

echo "Executing the startup script"
./startup.sh docker-compose.prod.yml --collect-static

