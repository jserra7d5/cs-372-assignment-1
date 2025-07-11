#!/usr/bin/env python3
"""
CREATED BY JOSEPH SERRA, ID: 934-512-465, 04/10/2025
Simple HTTP GET client using Python socket API
Downloads a small file from gaia.cs.umass.edu
"""

import socket

def main():
    host = "gaia.cs.umass.edu"
    port = 80
    uri = "/wireshark-labs/INTRO-wireshark-file1.html"
    
    # HTTP/1.1 requires Host header
    request = f"GET {uri} HTTP/1.1\r\nHost:{host}\r\n\r\n"
    
    print(f"Request: GET {uri} HTTP/1.1")
    print(f"Host:{host}")
    
    # Create TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        sock.send(request.encode('utf-8'))
        
        # Single recv() works for small files
        response = sock.recv(4096)
        response_str = response.decode('utf-8')
        
        print(f"[RECV] - length: {len(response_str)}")
        print(response_str)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()