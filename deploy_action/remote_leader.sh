#!/bin/bash


sudo su
# deploy
cd prod/
fileName="logs_$(date +"%m_%d_%Y__%H_%M").txt"
./main.sh | tee "$fileName"
