import socket
import subprocess

url = input("Digite a URL: ")

# Consulta de NS (Name Server)
try:
    ns_ips = socket.gethostbyname_ex(url)
    print("NS Records:", ns_ips)
    
    command = f"dig +short ns '{url}'"
    print(f"Executando comando: '{command}'")
    # Execute o comando usando subprocess ou outro método desejado
    subprocess.run(command, shell=True)
except socket.gaierror:
    print(f"Não foi possível resolver o nome de host para '{url}'")
