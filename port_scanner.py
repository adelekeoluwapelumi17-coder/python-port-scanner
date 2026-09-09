import socket

target= input("Enter an IP address")
print("scanning")

for port in range(1, 1025):
  sock = socket.socket()
  sock.settimeout(0.5)
  result = sock.connect_ex((target, port))
  if result == 0:
    print("port", port, "is OPEN")
    try:
      service = socket.getservbyport(port)
    except OSError:
      service = "Unknown"
    print("Service:", service)
  sock.close()
