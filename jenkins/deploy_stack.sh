#!/bin/bash

# This is to deploy the stack so it available to the end user which the stack can also perform rollind updates 

scp -i ~/.shh/ansible_id_rsa docker-compose.yaml jenkins@swarm-master:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/ansible_id_rsa jenkins@swarm-master << EOF
    export DATABASE_URI=${DATABASE_URI}
    export AUTHOR=${AUTHOR}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml pokemon-stack
EOF