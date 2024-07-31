# ProxyOrganizer

Organizes given proxies into HTTP/HTTPS, SOCKS, and Other files.

### File Locations
- Edit the file paths `input_file_path` and `output_dir` to suit your needs.
  - The file path for `input_file_path` must be an absolute path to the file you want it to pull from.
    - Example: "C:\Users\Lego\Downloads\proxys.txt"
  - The file path for `output_dir` must be absolute and should lead to a folder/directory.
    - Example: "C:\Users\Lego\Downloads\output example"

### Requirements
- Python3
- For ProxyOrganizerV2.py:
  - aiohttp==3.8.4
  - alive-progress==3.1.4

### Installation
To install the required packages for ProxyOrganizerV2.py, run:
pip install aiohttp==3.8.4 alive-progress==3.1.4

### Usage
- **ProxyOrganizer.py**: Optimized for speed, it organizes proxies by ports but does not perform further checks.
  - Example usage:
    ```
    python ProxyOrganizer.py
    ```

- **ProxyOrganizerV2.py**: Focused on accuracy and efficiency. Recommended for small quantities of proxies as it is not fast with large amounts.
  - Example usage:
    ```
    python ProxyOrganizerV2.py
    ```

### File Outputs for V2
- **http_proxies.txt**: Contains HTTP proxies.
- **https_proxies.txt**: Contains HTTPS proxies.
- **socks4_proxies.txt**: Contains SOCKS4 proxies.
- **socks5_proxies.txt**: Contains SOCKS5 proxies.
- **other_proxies.txt**: Contains other types of proxies.
- **failed_proxies.txt**: Contains proxies that failed to be categorized.

# From LegoLovesYou<3

