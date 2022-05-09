#!/usr/bin/env bash

# shellcheck disable=SC2086

# Usage:
#     part2-q5.sh cpu/mem <filename>

# local function to join words with comma
function join_words() {
  a=""
  for i in "$@";
  do
    a=$a"$i"",";
  done;
  echo "$a"
}
# check if user is root or not
# sudo/root is rquired to fetch proces name with SS tool
if [[ $USER != "root" ]];
then
  echo "Error: run me with sudo or root"
  exit 1
fi

# get user input for sort by if none passed in arguments
if [[ -z $1 ]];
then
  read -r -p "Enter Process Sort by (cpu/mem): " PROCESS_SORT
else
  PROCESS_SORT=$1
fi

# hardcoded pick only 3rd from top
process_details=$(ps -eo pid,%mem,%cpu,comm --sort=-%"$PROCESS_SORT" | sed -n '4p')

# find pid/cpu/mem/process name
pid=$(echo $process_details | cut -d " " -f1)
cpu=$(echo $process_details | cut -d " " -f2)
mem=$(echo $process_details | cut -d " " -f3)
process_name=$(echo $process_details | cut -d " " -f4)

# list local listening port by pid
local_listen_port_details=$(ss -ntulp4 state LISTENING | grep -i "pid=$pid")

count_lines=$(ss -ntulp4 state LISTENING | grep -ic "pid=$pid")

# compare how many local ports are listening for given process
if [ "$count_lines" -eq 0 ];
then
  port=""
else
  if [ "$count_lines" -eq 1 ];
  then
    port=$(echo -n $local_listen_port_details |  awk '{print $4}' | cut -d ":" -f2)
  else
    ports=$(ss -4 -ntulp state LISTENING | grep -i "pid=$pid" |  awk '{print $4}' | cut -d ":" -f2)
    port=$(join_words $ports)
  fi
fi

echo "Process Name:" $process_name  "CPU: "$cpu "MEM:" $mem "Port(s):" $port "PID:" $pid >> $2.log
