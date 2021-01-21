#!/bin/bash

declare -a secrets=("prod/db_url" "SATOSHI" "prod/simplez_keyz")
for i in "${secrets[@]}"
do
  echo "Handling secret $i"
  aws secretsmanager get-secret-value --secret-id $i --version-stage AWSCURRENT | jq -r '.SecretString' | jq -s add - env.json > temp_env.json
  cp temp_env.json env.json
done
