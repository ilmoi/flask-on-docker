#!/bin/bash

touch secret/env.json
touch secret/temp_env.json

declare -a secrets=("prod/db_url" "SATOSHI" "prod/simplez_keyz")

for i in "${secrets[@]}"
do
  echo "Handling secret $i"
  aws secretsmanager get-secret-value --secret-id $i --version-stage AWSCURRENT | jq -r '.SecretString' | jq -s add - secret/env.json > secret/temp_env.json
  cp secret/temp_env.json secret/env.json
done
