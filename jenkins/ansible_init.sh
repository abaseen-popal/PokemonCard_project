#!/bin/bash

mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
sudo apt install python3
sudo apt install python3-pip

pip3 install --user ansible

cd ansible && /home/jenkins/.local/bin/ansible-playbook -i inventory playbook.yaml
