
#!/bin/bash

# Build and push images
curl https://get.docker.com | sudo bash
sudo usermod -aG docker $(whoami)
sudo usermod -aG docker jenkins
sudo su - jenkins
sudo curl -L https://github.com/docker/compose/releases/download/1.27.4/docker-compose-\$(uname -s)-\$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

set pass {mypassword}

docker login --username={dockerhub_username} --email={dockerhub_email}

expect "password: "
send "$pass"
expect "password: "
send "$pass"