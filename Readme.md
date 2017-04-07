# Assignment 1
Docker Image containes Centos 6.8, Python 2.7.13 , MongoDB 3.0 and Tomcat Server 7.0

### Build Docker Image
Run Using below mentioned Command in the root folder.

```
docker build -t docker_test .
```

### Running Docker Container
Run the Docker container using below mentioned Command.

```
docker run -p 7080:8080 -itd docker_test
```

### To check Tomcat Server
Open your browser

```
http://<ip address of host machine>:7080
```
# Assignment 2
This is shell Script to execute commands on remote hosts.

### How Run it
Make it Executeble first
Using below mentioned command
```
chmod +x assignment2\executor.sh
```

Use below mentioned command to Run the shell script

```
./assignment2\executor.sh hostname1 hostname2 hostname3
```

### Notes*
* It take hostname as a list of arguments.
* ```hostname should be space separated not commma```.
* if no hostname is provided it will give this OutPut``` No Remote Hosts provided ``` and exit.
* Script will ask for ```Default User name ``` to SSH.
* Script prompt for command to excecute on remote hosts.
* It will ssh every time you submit a commmand to script.
* It is using ```22``` as default ssh port.
