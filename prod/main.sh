# script to be run on the server, to deploy the application

# Ensure that $ENV_PATH is set
# You may use the export command to do like this or update the .bashrc
# export ENV_PATH="/workspaces/cred/.env"

# Ensure that docker is installed


REPO_URL=https://github.com/CDCRC-IITRPR/cdcrc_website

set -e

# TODO: Add Logic to see if Commit ID Changed


echo "Cloning the repo"
# Clone the repo if the directory doesn't exist
[ ! -d "/path/to/dir" ] && git clone "$REPO_URL"

cd cdcrc_website

git fetch --all

# changing the branch
git reset --hard origin/prod

echo "Moving the env file from the \$ENV_PATH to current directory"
cp $ENV_PATH ./

sudo chmod +x startup.sh

# adding the command in nginx/Dockerfile.prod to use the ssl config
cat <<'EOT' >> nginx/Dockerfile.prod
COPY nginx_with_ssl.conf /etc/nginx/conf.d/nginx.conf
EOT


# Building 
echo "Build the application"
docker-compose -f docker-compose.prod.yml build

echo "Start the application"
docker-compose -f docker-compose.prod.yml up -d

echo "Executing the startup script"
./startup.sh docker-compose.prod.yml --collect-static

