Here’s a single README file combining both projects into a concise description:  

---

# FTP Client and Server Implementation  

## Description  
This repository contains two implementations of a simple FTP client-server system. Both versions allow file transfers between a client and a server over a specified TCP port, with files transmitted in 1KB chunks for efficient handling of large files.  

### 1. Basic FTP Client-Server  
- Implements a single-threaded FTP server that listens for client connections.  
- The client can issue commands to upload and download files.  
- Designed for educational purposes, with a simplified approach to file transfer.  

### 2. Multi-threaded FTP Client-Server  
- Enhances the basic implementation by supporting multiple concurrent client connections using threads.  
- Each client connection is handled by a separate thread, allowing simultaneous file transfers.  
- Includes additional error handling and optimizations for improved performance.  

## Features  
- **File Transfer**: Supports `get <filename>` (download) and `upload <filename>` (upload) commands.  
- **Chunk-Based Transmission**: Files are transferred in 1KB chunks to prevent memory overload.  
- **Multi-threading Support** (for the second implementation): Allows multiple clients to connect simultaneously.  
- **Port Configurability**: Default server port is 5106 but can be modified.  

## How to Run  

### Start the Server  
```bash
~ python3 ftpserver 5106
```  

### Start the Client  
```bash
~ python3 ftpclient 5106
```  

### Client Commands  
- Download a file: `get filename`  
- Upload a file: `upload filename`  

## Dependencies  
- Python implementation uses `socket`, `os`, and `threading` libraries.  
- Basic knowledge of networking and command-line execution is helpful.  

## Notes  
- This implementation does not conform to the official FTP standard but serves as a learning tool for understanding file transfer over TCP.  

---
