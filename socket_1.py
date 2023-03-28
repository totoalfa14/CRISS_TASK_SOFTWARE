import socket
ServerIP = "172.17.29.11"
ServerPORT = 6000

serveraddress=(ServerIP,ServerPORT)
buffersize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

message = "2022A4PS0673P"

bytetosend = str.encode(message)

UDPClientSocket.sendto(bytetosend,serveraddress)


