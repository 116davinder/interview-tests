#!/bin/bash

TMP_DIR=$(mktemp -d)
OUTPUT_FILE=/tmp/access.log

rm -rf $OUTPUT_FILE

tar -xzf ./archive.tar.gz -C $TMP_DIR

for file in $TMP_DIR/*.log;
do
    while read -r line
    do
      read -r time status ip <<< $line
      if [ "$ip" != "127.0.0.1" ]; then
          if [[ $status =~ ^5 ]]; then
             echo $line >> $OUTPUT_FILE
          fi
      fi
    done < $file
done

rm -rf $TMP_DIR
