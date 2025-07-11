# Socket Programming Assignment

## Files Overview

1. **simple_get.py** - Basic HTTP GET client for small files
2. **large_file_get.py** - HTTP GET client with loop for large files  
3. **simple_server.py** - Simple HTTP server

## How to Run

### Client Programs
```bash
# Get small file
python3 simple_get.py

# Get large file
python3 large_file_get.py
```

### Server Program
```bash
# Start server on localhost:8080
python3 simple_server.py
```

Then open browser to: `http://127.0.0.1:8080`

## Expected Output

- **Clients**: HTTP response with headers and HTML content
- **Server**: Connection logs and request details, serves HTML response to browser
