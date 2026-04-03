# Network Scanner Lab Project

## Overview
This project is a simple Python-based TCP port scanner built to understand how network scanning works at a fundamental level. It simulates basic functionality of tools like Nmap by attempting TCP connections to identify open ports.

---

## Features
- Single-port scanning
- Port range scanning
- Service detection for common ports (HTTP, SMB, RDP, etc.)
- Input validation for port ranges
- Scan duration tracking
- Comparison with Nmap results

---

## How It Works
The scanner uses Python’s `socket` library to attempt TCP connections to specified ports. If a connection is successful, the port is considered open.

---

## Usage

Run the script:

```bash
python3 scanner.py
```

Then enter:
- Target IP address
- Start port
- End port

---

## Example Output

```
Scanning 172.16.94.130 from port 440 to 450...

Port 445 is OPEN (SMB)

Scan complete. Total open ports found: 1
Scan time: 11.02 seconds
```

---

## Comparison with Nmap

Results were compared with Nmap to validate accuracy.

- Both tools detected port 445 as open.
- Nmap identified additional ports as "filtered".
- The custom scanner cannot distinguish between closed and filtered ports.

---

## Limitations
- Slower than Nmap
- Uses only TCP connect scanning
- Cannot detect filtered ports
- Limited service detection

---

## Skills Demonstrated
- Python programming (loops, conditionals, input handling)
- Networking fundamentals (TCP, ports, services)
- Basic cybersecurity concepts (port scanning, reconnaissance)
- Git and GitHub workflow
- Problem-solving and debugging

---

## Lab Environment
All scans were performed in a private home lab environment using systems I own and control.

---

## Project Structure

```
network-scanner/
├── scanner.py
├── README.md
├── docs/
│   ├── step1-*.png
│   ├── step2-*.png
│   ├── step3-*.png
│   ├── step4-*.png
│   ├── step5-*.png
│   ├── step6-*.png
└── examples/
```

---

## Future Improvements
- Add multithreading for faster scanning
- Export results to a file
- Add UDP scanning
- Improve service detection
