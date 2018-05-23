#!/bin/bash
current_date=`date '+%Y-%m-%d'`
output_filename=$(echo $1)_$current_date.tar.bz2

if [ $# -eq 0 || $# -gt 1 ]
then
    echo ""
    echo "Please pass source dir"
    echo "usage: ./compress.sh <source dir>"
    echo ""
    echo "example"
    echo "./compress.sh /var/data"
elif [ $# -gt 0 ]
    if [ -f "$output_filename" ]
    then
        echo "$output_filename is already there"
        exit 1
    else
        tar -cjf $output_filename $1
        exit 0
    fi
fi