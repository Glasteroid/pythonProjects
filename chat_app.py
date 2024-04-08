import socket
 
# Create a TCP/IP socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Define host 
host = 'localhost'
 
# define the communication port 
port = 8080
 
# Bind the socket to the port 
sock.bind((host, port))
# Listen for incoming connections 
sock.listen(1)
 
# Wait for a connection 
print('waiting for a connection')
connection, client = sock.accept()
 
print(client, 'connected')
 
# Receive the data in small chunks and retransmit it 
 
data = connection.recv(16)
print('received "%s"' % data)
if data:
 
    connection.sendall(data)
else:
    print('no data from', client)
 
 
# Close the connection 
connection.close()