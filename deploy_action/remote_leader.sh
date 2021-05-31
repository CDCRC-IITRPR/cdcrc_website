#!/bin/bash


sudo ENV_PATH="$ENV_PATH" su


set -e
set -o pipefail

# ! ensure that this is below the sudo su command
logs_dir_name="logs"

# deploy
cd prod/

# making logs directory if not exist
mkdir -p "$logs_dir_name"

fileName="logs_$(date +"%m_%d_%Y__%H_%M").txt"
echo "Dumping logs file in $logs_dir_name/$fileName"

echo "Executing main script..."
./main.sh |& tee "$logs_dir_name/$fileName"

if [ $? -ne 0 ]; then
    echo "Error Occurred! Exiting..."
    exit 1
fi

echo "Victorious Remote Leader returned in triumph!"

