#!/bin/bash

# Getting default ssh user
echo "Please enter the default user for ssh:"
read default_user

# Getting command to execute on remote hosts
echo "Please enter the SSH command to execute:"
read ssh_command

# Executing Command on Remote Hosts
for HOSTNAME in "$@" ; do
    ssh -l ${default_user} ${HOSTNAME} "${ssh_command}"
done
