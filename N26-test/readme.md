Solution.py is not complete is copy from https://github.com/paulc/dnslib/blob/master/dnslib/proxy.py

It should be modified 
1. To parse the DNS Request Query ( from Socket Stream )
2. send request to upstream server
3. recieve response from upstream server
4. send response to DNS Query ( To Socket Stream )

Ref:
1. https://developers.google.com/speed/public-dns/docs/secure-transports
