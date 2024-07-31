import os

# Change the file path to suit your needs
input_file_path = r"C:\Users\Lego\Downloads\BOT_PROXYs.txt"

# Change the file path to suit your needs
output_dir = r"C:\Users\Lego\projects\LegoHitsYou\proxys\bot proxies"
http_https_path = os.path.join(output_dir, "http_https_proxies.txt")
socks_path = os.path.join(output_dir, "socks_proxies.txt")
other_path = os.path.join(output_dir, "other_proxies.txt")

http_https_ports = {
    80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
    443, 591, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009, 8010, 
    8011, 8012, 8013, 8014, 8015, 8016, 8017, 8018, 8019, 8020, 8080, 8081, 8082, 
    8083, 8084, 8085, 8086, 8087, 8088, 8089, 8090, 8888, 8880, 8443, 3128, 3132, 
    9000, 9080, 9443, 10443
}

socks_ports = {
    1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 2080, 4153, 
    4145, 9050, 9051, 9052, 9150, 9151, 10811, 12345, 34567, 65535
}


http_https_proxies = []
socks_proxies = []
other_proxies = []

with open(input_file_path, 'r') as file:
    for line in file:
        proxy = line.strip()
        if proxy:
            parts = proxy.split(':', 1)
            if len(parts) == 2:
                ip, port = parts
                try:
                    port = int(port)
                    if port in http_https_ports:
                        http_https_proxies.append(proxy)
                    elif port in socks_ports:
                        socks_proxies.append(proxy)
                    else:
                        other_proxies.append(proxy)
                except ValueError:
                    other_proxies.append(proxy)
            else:
                other_proxies.append(proxy)

with open(http_https_path, 'w') as file:
    file.write("\n".join(http_https_proxies))

with open(socks_path, 'w') as file:
    file.write("\n".join(socks_proxies))

with open(other_path, 'w') as file:
    file.write("\n".join(other_proxies))
