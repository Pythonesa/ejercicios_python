from scapy.all import sr1, IP, TCP

def check_port(ip_address, port):
    try:
        packet = sr1(IP(dst=ip_address) / TCP(dport=port, flags="S"), timeout=1)
        if packet and packet.haslayer(TCP) and packet[TCP].flags == 0x12:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al enviar el paquete: {e}")
        return False
    
ip = input("Ingresa la IP: ")
port = int(input("Ingresa el puerto: "))

if check_port(ip, port):
    print("El puerto esta abierto")
else:
    print("El puerto esta cerrado")