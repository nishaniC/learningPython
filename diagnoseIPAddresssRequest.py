import requests
import sys

def print_usage_and_exit(code):
    print("Usage: python script.py <host> [port]")
    sys.exit(code)

# Argument validation
if len(sys.argv) not in [2, 3]:
    print("Error: Invalid number of arguments.")
    print_usage_and_exit(1)

# host = sys.argv[1]
port = 80

if len(sys.argv) == 3:
    try:
        port = int(sys.argv[2])
        if not (1 <= port <= 65535):
            raise ValueError
    except ValueError:
        print("Error: Port must be an integer between 1 and 65535.")
        sys.exit(2)
host = sys.argv[1]
try:
    # it’s addressing its efforts to port 3001, while our server is listening at port 3000
    reply = requests.head(host,timeout=10)
    reply.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
except requests.exceptions.RequestException:
    print("Nobody's home, sorry!")

else:
    print('Everything fine!')