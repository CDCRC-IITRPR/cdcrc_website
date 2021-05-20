# script to be run on the server, to deploy the application

# Ensure that $ENV_PATH is set
# You may use the export command to do like this or update the .bashrc
# export ENV_PATH="/workspaces/cred/.env"

# Ensure that docker is installed

set -e

# TODO: Add Logic to see if Commit ID Changed


echo "Cloning the repo"
# Remove the directory if it exist
rm -rf cdcrc_website
git clone https://github.com/vinx-2105/cdcrc_website

cd cdcrc_website

echo "Moving the env file from the \$ENV_PATH to current directory"
cp $ENV_PATH ./

sudo chmod +x startup.sh

# Building 
echo "Build the application"
docker-compose -f docker-compose.prod.yml build

echo "Start the application"
docker-compose -f docker-compose.prod.yml up -d

echo "Executing the startup script"
./startup.sh

