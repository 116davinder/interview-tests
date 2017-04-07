#!/bin/bash

# Getting default ssh user
echo "Please enter the default user for ssh:"
read default_user

while [ "$do_command_continue" != "no" ]
do 
	# Getting command to execute on remote hosts
	echo "Please enter the SSH command to execute:"
	read ssh_command
	
	# Executing Command on Remote Hosts
	for HOSTNAME in "$@" ; do
	    ssh -l ${default_user} ${HOSTNAME} -p 22 "${ssh_command}"
	done

	echo "if you donot want to execute more commands ? Press 'no' "
	read do_command_continue
done
