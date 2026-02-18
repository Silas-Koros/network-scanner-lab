import socket

target_ip = input("Enter the target IP address: ").strip()
target_port = int(input("Enter port Number: ").strip())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)

result = sock.connect_ex((target_ip, target_port))

if result == 0:
	print(f"Port {target_port} is OPEN on {target_ip}")
else:
	print(f"Port {target_port} is CLOSED or FILTERED on {target_ip}")

sock.close()
