## Part 3 Question 5
Shell script to take third most CPU & Memory consuming process, this should output to output file with the following properties
* Process Name
* % CPU  used
* % Memory used  
* PORT
* PID

### Parameters
* first parameter must be either `cpu` or `mem`
* second parameter must be `filename` or `path` without extension

### Requirements
* Linux based system is supported.
* `ss` util should be installed aka `netstat`.
* you must have `sudo`/`root` access to the system.

### Notes*
* if `0` port is being used then output will be empty string.
* if multiple ports are being used then comma separate list will added in output.

### Usage
```bash
$ sudo ./part2-q5.sh cpu stats-logs
$ cat stats-logs.log
Process Name: firefox-bin CPU: 3.5 MEM: 5.2 Port(s): PID: 4655
```
