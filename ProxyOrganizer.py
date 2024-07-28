import os

# Define the input file path
input_file_path = "C:\\Users\\Lego\\LegoHitsYou\\proxys\\BOT_PROXYs.txt" # Replace with where you want it to get the proxies, path must be absolute

# Define the output file paths
output_dir = "C:\\Users\\Lego\\LegoHitsYou\\proxys" # Replace with where you want the files to be sent to
http_https_path = os.path.join(output_dir, "http_https_proxies.txt")
socks_path = os.path.join(output_dir, "socks_proxies.txt")
other_path = os.path.join(output_dir, "other_proxies.txt")

# Port classifications
http_https_ports = {80, 8080, 8000, 3128}
socks_ports = {1080, 1081, 1085, 1088, 4145}

# Lists to hold categorized proxies
http_https_proxies = []
socks_proxies = []
other_proxies = []

# Read the input file and categorize proxies
with open(input_file_path, 'r') as file:
    for line in file:
        proxy = line.strip()
        if proxy:
            ip, port = proxy.split(':')
            port = int(port)
            if port in http_https_ports:
                http_https_proxies.append(proxy)
            elif port in socks_ports:
                socks_proxies.append(proxy)
            else:
                other_proxies.append(proxy)

# Save the categorized proxies to their respective files
with open(http_https_path, 'w') as file:
    file.write("\n".join(http_https_proxies))

with open(socks_path, 'w') as file:
    file.write("\n".join(socks_proxies))

with open(other_path, 'w') as file:
    file.write("\n".join(other_proxies))
