# Find the IP address and hostname with python

import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Since IP can change, you might be getting a different value of IP on every run

print("Computer Name : " + hostname)
print("IP Address    : " + ip_address)
