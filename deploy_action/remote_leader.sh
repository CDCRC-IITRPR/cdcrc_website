#!/bin/bash

set -e

sudo ENV_PATH="$ENV_PATH" su

# ! ensure that this is below the sudo su command
logs_dir_name="logs"

# deploy
cd prod/
echo $ENV_PATH
# source ./bashrc
echo $ENV_PATH

# making logs directory if not exist
mkdir -p "$logs_dir_name"

fileName="logs_$(date +"%m_%d_%Y__%H_%M").txt"
echo "Dumping logs file in $logs_dir_name/$fileName"

./main.sh 2>&1 | tee "$logs_dir_name/$fileName"

echo "Victorious Remote Leader returned in triumph!"

