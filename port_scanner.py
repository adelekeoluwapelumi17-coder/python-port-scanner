import socket

target= input("Enter an IP address")
print("scanning")

for port in range(1, 11)
  sock = socket.socket()
  sock.settimeout(0.5)
  result = sock.connect_ex((target, port))
  if result == 0:
    print("port", port, "is OPEN")
  sock.close()
