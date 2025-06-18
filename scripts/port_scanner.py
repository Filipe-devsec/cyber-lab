import socket
from datetime import datetime

# Lista de portas "comuns" para fazer scann
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

# Pergunta o host ao user
target = input("Introduz o IP ou domínio para fazer scan: ")

print(f"\nInício do scan em {target} às {datetime.now()}")
print("-" * 40)

# Tenta conectar às portas
for port, service in common_ports.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # tempo limite por porta (segundos)

    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Porta {port} ({service}): ABERTA")
    else:
        print(f"Porta {port} ({service}): fechada")

    sock.close()

print("\nScan concluído.")
