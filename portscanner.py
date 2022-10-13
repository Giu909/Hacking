import socket
import termcolor

def scan (target, ports):
    for port in range(1,ports):
            scan_port(target, port)

def scan_port (ipaddress, port):
    try:
        #Socket Init
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Open " + str(port))
        sock.close()
    except:
        print("[-] Port Closed " + str(port))

targets = input("[*] Enter Targets To Scan (Separate by ','): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets,ports)



