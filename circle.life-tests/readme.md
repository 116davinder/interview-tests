# Challenge 1
Create Subnet from given IP address and given total number of subnets.

### Prerequisite
```
sipcalc-1.1.6 or higher on linux box. 
```
### Usage
```
bash subnetter.sh 192.168.0.0/24 2
```

### Output
```
[davinder@test circle.life-tests]$ bash subnetter.sh 192.168.0.0/24 4
subnet=192.168.0.0/24 network=192.168.0.0 broadcast=192.168.0.255 gateway=192.168.0.1 hosts=253
subnet=192.168.1.0/24 network=192.168.1.0 broadcast=192.168.1.255 gateway=192.168.1.1 hosts=253
subnet=192.168.2.0/24 network=192.168.2.0 broadcast=192.168.2.255 gateway=192.168.2.1 hosts=253
subnet=192.168.3.0/24 network=192.168.3.0 broadcast=192.168.3.255 gateway=192.168.3.1 hosts=253
```
