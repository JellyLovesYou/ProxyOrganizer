import os
import socket
import asyncio
import aiohttp
from alive_progress import alive_bar

# Define the input file path
input_file_path = r"C:\Users\Lego\Downloads\BOT_PROXYs.txt"

# Define the output file paths
output_dir = r"C:\Users\Lego\LegoHitsYou\proxys"
http_path = os.path.join(output_dir, "http_proxies.txt")
https_path = os.path.join(output_dir, "https_proxies.txt")
socks4_path = os.path.join(output_dir, "socks4_proxies.txt")
socks5_path = os.path.join(output_dir, "socks5_proxies.txt")
other_path = os.path.join(output_dir, "other_proxies.txt")
failed_path = os.path.join(output_dir, "failed_proxies.txt")

# Lists to hold categorized proxies
http_proxies = []
https_proxies = []
socks4_proxies = []
socks5_proxies = []
other_proxies = []
failed_proxies = []

async def test_proxy(proxy, session):
    ip, port = proxy.split(':')
    port = int(port)

    # Early exit if one test succeeds
    result = 'FAILED'

    async def test_socks4():
        try:
            reader, writer = await asyncio.wait_for(asyncio.open_connection(ip, port), timeout=5)
            writer.write(b'\x04\x01' + port.to_bytes(2, 'big') + socket.inet_aton('0.0.0.0') + b'\x00')
            await writer.drain()
            response = await reader.read(8)
            writer.close()
            await writer.wait_closed()
            if response[0] == 0x00 and response[1] == 0x5A:
                return 'SOCKS4'
        except asyncio.TimeoutError:
            return 'FAILED'
        except:
            return 'FAILED'

    async def test_socks5():
        try:
            reader, writer = await asyncio.wait_for(asyncio.open_connection(ip, port), timeout=5)
            writer.write(b'\x05\x01\x00')
            await writer.drain()
            response = await reader.read(2)
            writer.close()
            await writer.wait_closed()
            if response[0] == 0x05 and response[1] == 0x00:
                return 'SOCKS5'
        except asyncio.TimeoutError:
            return 'FAILED'
        except:
            return 'FAILED'

    async def test_http():
        try:
            async with session.get('http://example.com', proxy=f'http://{proxy}', timeout=5) as response:
                if response.status == 200:
                    return 'HTTP'
        except asyncio.TimeoutError:
            return 'FAILED'
        except:
            return 'FAILED'

    async def test_https():
        try:
            async with session.get('https://example.com', proxy=f'http://{proxy}', timeout=5) as response:
                if response.status == 200:
                    return 'HTTPS'
        except asyncio.TimeoutError:
            return 'FAILED'
        except:
            return 'FAILED'

    # Run all tests concurrently and stop at the first success
    tests = [test_http(), test_https(), test_socks4(), test_socks5()]
    for test in asyncio.as_completed(tests):
        try:
            result = await asyncio.wait_for(test, timeout=5)
            if result != 'FAILED':
                return result
        except asyncio.TimeoutError:
            continue

    return 'FAILED'

async def process_proxies(proxies, session):
    results = []
    total_proxies = len(proxies)
    with alive_bar(total_proxies, title='Checking proxies') as bar:
        for proxy in proxies:
            result = await test_proxy(proxy, session)
            results.append(result)
            print(f"{len(results)}/{total_proxies} Proxy: {proxy} Type: {result}")
            bar()
    return results

async def main():
    with open(input_file_path, 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]

    async with aiohttp.ClientSession() as session:
        results = await process_proxies(proxies, session)

    for proxy, proxy_type in zip(proxies, results):
        if proxy_type == 'HTTP':
            http_proxies.append(proxy)
        elif proxy_type == 'HTTPS':
            https_proxies.append(proxy)
        elif proxy_type == 'SOCKS4':
            socks4_proxies.append(proxy)
        elif proxy_type == 'SOCKS5':
            socks5_proxies.append(proxy)
        else:
            failed_proxies.append(proxy)

    # Save the categorized proxies to their respective files
    with open(http_path, 'w') as file:
        file.write("\n".join(http_proxies))

    with open(https_path, 'w') as file:
        file.write("\n".join(https_proxies))

    with open(socks4_path, 'w') as file:
        file.write("\n".join(socks4_proxies))

    with open(socks5_path, 'w') as file:
        file.write("\n".join(socks5_proxies))

    with open(other_path, 'w') as file:
        file.write("\n".join(other_proxies))

    with open(failed_path, 'w') as file:
        file.write("\n".join(failed_proxies))

if __name__ == "__main__":
    asyncio.run(main())
