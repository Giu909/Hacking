import socket
import termcolor

def scan (targets, ports):
    for target in targets:
        print("[*] Targetting " + str(target))
        for port in range(1, ports):
            scan_port(target, port)

def scan_port (ipaddress, port):
    try:
        #Socket Init
        sock = socket.socket()
        sock.connect((ipaddress.trim(' '), port))
        print("[+] Port Opened " + str(port) + " " + str(ipaddress.strip(' ')))
        sock.close()
    except:
        print("[-] Port Closed " + str(port) + " " + str(ipaddress.strip(' ')))

targets = input("[*] Enter Targets To Scan (Separate by ','): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

scan(targets.split(','), ports)


