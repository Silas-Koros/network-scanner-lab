import socket

target_ip = input("Enter target IP address: ").strip()
start_port = int(input("Enter start port: ").strip())
end_port = int(input("Enter end port: ").strip())

if start_port > end_port:
    print("Error: start port must be less than or equal to end port.")
else:
    print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")

    open_ports = 0

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports += 1

        sock.close()

    if open_ports == 0:
        print("No open ports were found in this range.")

    print(f"\nScan complete. Total open ports found: {open_ports}")
