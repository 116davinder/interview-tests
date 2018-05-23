#!/bin/bash

if [ "$#" == 0 ];
then
    echo "Usage: <script> 192.168.1.1/24 2"
    exit 1
fi

givenSubnetCount="$2"
givenSubnetIp=$(echo $1 | cut -d "/" -f1)                                 # 192.168.0.0/x
givenSubnetCidr=$(echo $1 | cut -d "/" -f2)
givenSubnetCidrCheck=$(echo $1 | grep /)                                  # /24
givenIpOctetA=$(echo $givenSubnetIp | cut -d "." -f1)

if [ $givenIpOctetA -ge 224 ];
then
    echo "address doesn't belong to a,b,c class"
    exit 1
fi

calculatedSubnets=$(sipcalc $1 -n $givenSubnetCount | grep -w Network | cut -d "-" -f2)

for i in $calculatedSubnets
do
    broadcastAdrress=$(sipcalc $i/$givenSubnetCidr | grep "Broadcast address" | cut -d "-" -f2 | sed 's/ //g')
    gatewayAdrress=$(sipcalc $i/$givenSubnetCidr | grep "Usable range" | cut -d "-" -f2 | sed 's/ //g')
    networkAddress=$(sipcalc $i/$givenSubnetCidr | grep "Network address" | cut -d "-" -f2 | sed 's/ //g')
    totalHosts=$(sipcalc $i/$givenSubnetCidr | grep "Addresses in network" | cut -d "-" -f2 | sed 's/ //g')
    useablehosts=$(($totalHosts - 3))
    echo "subnet="$networkAddress/$givenSubnetCidr "network="$networkAddress "broadcast="$broadcastAdrress "gateway="$gatewayAdrress "hosts="$useablehosts
done
