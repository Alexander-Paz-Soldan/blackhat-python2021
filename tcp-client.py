import socket

# hard-coded defaults
target_host = "www.google.com"
target_port = 80
#
print("Provide target host (for example www.google.com)")
target_host = input()
print("provide the port (for example port 80)")
try:
    target_in = input()
    target_port = int(target_in)
except:
    print("not an integer defaulting to port 80")
    target_port = 80
print("host:{target_host} port:{target_port}",(target_host, target_port))
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client
client.connect((target_host, target_port))
# send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
# receive data back
response = client.recv(4096)
print(response.decode())
client.close()
print("End of program did you receive anything?")

# if all is right a message that this document has moved is displayed.
