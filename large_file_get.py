#!/usr/bin/env python3
"""
CREATED BY JOSEPH SERRA, ID: 934-512-465, 04/10/2025
HTTP GET client for large files using Python socket API
Downloads a large file from gaia.cs.umass.edu using recv loop
"""

import socket

def main():
    host = "gaia.cs.umass.edu"
    port = 80
    uri = "/wireshark-labs/HTTP-wireshark-file3.html"
    
    # HTTP/1.1 requires Host header
    request = f"GET {uri} HTTP/1.1\r\nHost:{host}\r\n\r\n"
    
    print(f"Request: GET {uri} HTTP/1.1")
    print(f"Host:{host}")
    
    # Create TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        sock.send(request.encode('utf-8'))
        
        # Receive in chunks until connection closes
        response_data = b""
        chunk_size = 1024
        
        while True:
            chunk = sock.recv(chunk_size)
            if len(chunk) <= 0:
                break  # Server closed connection
            response_data += chunk
        
        response_str = response_data.decode('utf-8')
        print(f"[RECV] - total length: {len(response_str)}")
        print(response_str)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()