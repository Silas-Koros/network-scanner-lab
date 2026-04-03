# Network Scanner Lab Project

This project is a Python-based port scanner built for learning how network scanning works.

Lab use only.

## Progress Log

### Step 1
Built a basic single-port TCP connect scanner in Python.

### Step 2
Expanded the scanner to scan a small range of ports and print open ports.

### Step 3
Improved the scanner by adding:
- port range validation
- open port counting
- cleaner output
- a summary message after the scan

## Step 3 Test
Target: 192.168.72.128 (Windows VM)
Range tested: 440-450
Observed open port: 445

### Step 4
Added basic service detection using common port mapping (e.g., SMB, HTTP, RDP).

### Step 5
Added scan timing so the scanner reports how long the scan took to complete.

## Step 5 Test
Target: 192.168.72.128 (Windows VM)
Range tested: 440-450
Observed open port: 445 (SMB)
New feature: scan duration display

## Step 6 — Comparison with Nmap

To validate the scanner, results were compared with Nmap.

### Python Scanner Result
- Detected open port: 445 (SMB)

### Nmap Result
- 445/tcp open (microsoft-ds)
- Other ports reported as filtered

### Observations
- Both tools identified port 445 as open.
- Nmap provides more detailed service names.
- Nmap detected multiple ports as "filtered", while the custom scanner could not distinguish between closed and filtered ports.
- The custom scanner uses a simple TCP connect method, which limits detection accuracy.

### Conclusion
The custom scanner successfully demonstrates how port scanning works, but lacks the advanced detection capabilities and accuracy of professional tools like Nmap.

