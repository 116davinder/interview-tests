#!/bin/bash

if [ $# -eq 0 ]; then
    echo "No Remote Hosts provided"
    exit 1

else 
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
	    echo ""
	    echo "Printing SSH command OutPut"
	    ssh -l ${default_user} ${HOSTNAME} -p 22 "${ssh_command}"
	done

	echo "if you donot want to execute more commands ? Press 'no' "
	echo "else Press any key to continue"
	read do_command_continue
    done

fi
