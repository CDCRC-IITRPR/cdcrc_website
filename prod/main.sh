# script to be run on the server, to deploy the application

# Ensure that $ENV_PATH is set
# You may use the export command to do like this or update the .bashrc
# export ENV_PATH="/workspaces/cred/.env"

# Ensure that docker is installed


REPO_URL=https://github.com/CDCRC-IITRPR/cdcrc_website

set -e
set -o pipefail

# Clone the repo if the directory doesn't exist
if [ ! -d "./cdcrc_website/" ] 
then 
    echo "Cloning the repo.."
    git clone "$REPO_URL"
else
    echo "Directory Already exists!"
fi

echo "Changing directory to cdcrc_website/"
cd cdcrc_website

# changing the branch
git checkout prod --
git fetch --all
git reset --hard origin/prod

echo "Moving the env file from the \$ENV_PATH to current directory"
cp $ENV_PATH ./.env

sudo chmod +x startup.sh

# adding the command in nginx/Dockerfile.prod to use the ssl config
cat <<'EOT' >> nginx/Dockerfile.prod
COPY nginx_with_ssl.conf /etc/nginx/conf.d/nginx.conf
EOT


# Building 
echo "Building the application"
docker-compose -f docker-compose.prod.yml build 

echo "Stopping all containers"
docker-compose -f docker-compose.prod.yml down

echo "check if we need to renew any certificates"
certbot renew

echo "Removing static_webassets volume"
docker volume rm cdcrc_website_static_webassets

echo "Starting the application....."
docker-compose -f docker-compose.prod.yml up -d

echo "Executing the startup script"
./startup.sh docker-compose.prod.yml --collect-static

echo "Yipeee! Deployment complete."
