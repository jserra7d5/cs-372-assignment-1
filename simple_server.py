#!/usr/bin/env python3
"""
CREATED BY JOSEPH SERRA, ID: 934-512-465, 04/10/2025
Simple HTTP server using Python socket API
Listens on localhost and serves a simple HTML response
"""

import socket
import threading

def handle_client(client_socket, client_address):
    try:
        # Receive raw HTTP request bytes
        request = client_socket.recv(1024)
        print(f"Connected by {client_address}")
        print(f"Received: {request}")
        
        # Build HTTP response with required headers
        response_text = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=UTF-8\r\n\r\n"
            "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"
        )
        
        client_socket.send(response_text.encode('utf-8'))
        
        print("Sending>>>>>>>")
        print("HTTP/1.1 200 OK")
        print("Content-Type: text/html; charset=UTF-8")
        print("<html>Congratulations! You've downloaded the first Wireshark lab file!</html>")
        print("<<<<<<<<")
        
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()

def main():
    host = '127.0.0.1'  # localhost
    port = 8080
    
    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse address
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(5)  # Accept up to 5 queued connections
        
        print(f"HTTP Server listening on {host}:{port}")
        
        while True:
            # Block until client connects
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            
            # Handle each client in separate thread
            client_thread = threading.Thread(
                target=handle_client, 
                args=(client_socket, client_address)
            )
            client_thread.daemon = True
            client_thread.start()
            
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()