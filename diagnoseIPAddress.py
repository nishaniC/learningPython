import sys
import socket
import ssl

MAX_REDIRECTS = 5

def print_usage_and_exit(code):
    print("Usage: python script.py <host> [port]")
    sys.exit(code)

def send_head_request(host, port, use_https):
    try:
        raw_sock = socket.create_connection((host, port), timeout=5)
        sock = ssl.create_default_context().wrap_socket(raw_sock, server_hostname=host) if use_https else raw_sock

        request = f"HEAD / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        sock.sendall(request.encode())

        response = sock.recv(1024).decode(errors='ignore')
        sock.close()
        return response

    except socket.timeout:
        print("Error: Connection timed out.")
        sys.exit(3)
    except Exception as e:
        print(f"Error: Connection failed. ({e})")
        sys.exit(4)

def extract_location(headers):
    for line in headers:
        if line.lower().startswith("location:"):
            return line.split(":", 1)[1].strip()
    return None

def parse_host_and_port(url):
    if url.startswith("https://"):
        url = url[8:]
        port = 443
        use_https = True
    elif url.startswith("http://"):
        url = url[7:]
        port = 80
        use_https = False
    else:
        return None, None, None

    parts = url.split("/", 1)
    host = parts[0]
    return host, port, use_https

# Argument validation
if len(sys.argv) not in [2, 3]:
    print("Error: Invalid number of arguments.")
    print_usage_and_exit(1)

host = sys.argv[1]
port = 80

if len(sys.argv) == 3:
    try:
        port = int(sys.argv[2])
        if not (1 <= port <= 65535):
            raise ValueError
    except ValueError:
        print("Error: Port must be an integer between 1 and 65535.")
        sys.exit(2)

use_https = (port == 443)

# Redirect loop
redirect_count = 0
while redirect_count <= MAX_REDIRECTS:
    response = send_head_request(host, port, use_https)
    headers = response.splitlines()
    # clean and Pythonic way to safely extract the first line of an HTTP response header
    first_line = headers[0] if headers else "No response received."
    print(first_line)

    if first_line.startswith("HTTP/1.1 301") or first_line.startswith("HTTP/1.1 302"):
        location = extract_location(headers)
        if not location:
            print("Redirect status received, but no Location header found.")
            break

        print("Redirecting to:", location)
        parsed = parse_host_and_port(location)
        if not parsed[0]:
            print("Unsupported redirect URL format.")
            break

        host, port, use_https = parsed
        redirect_count += 1
    else:
        break

if redirect_count > MAX_REDIRECTS:
    print("Too many redirects.")