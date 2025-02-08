# FTP Client and Server Implementation

## Description
This project implements a simple version of an FTP client/server software. The system consists of two programs:

- **ftpserver**: A server that listens for client connections on a specified TCP port.
- **ftpclient**: A client that connects to the server and issues commands to transfer files.


https://github.com/user-attachments/assets/c8dad715-77f6-46d2-b07a-ea09a2dd17cb


### Workflow
1. The **ftpserver** is started on a computer and listens on a specified TCP port (e.g., 5106).
2. The **ftpclient** is executed on the same computer, providing the server's port number as a command-line argument:
   ```sh
   ftpclient 5106
   ```
3. The user can issue the following commands from the client:
   - `get <filename>`: Retrieves a file from the server.
   - `upload <filename>`: Uploads a file to the server.
4. Files are transmitted in chunks of **1 KB** to handle large files efficiently.

### Testing
During testing, the following steps will be performed:
1. The client will download **downloadTestFile.pptx** from the server and save it locally as **newDownloadTestFile.pptx**.
2. The client will upload **uploadTestFile.pptx** to the server, which will save it as **newUploadTestFile.pptx**.

Renaming the files with the prefix "new" prevents overwriting the original test files.

### Important Considerations
- Files are broken into smaller **1 KB** chunks and transmitted iteratively.
- If issues arise, use a small text file broken into smaller pieces for debugging.
- Always **flush the output** after each send to ensure data integrity.

### Note
This implementation does not conform to the official FTP standard but provides a simplified version for educational purposes.

