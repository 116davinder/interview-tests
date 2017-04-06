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
