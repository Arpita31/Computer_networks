### **FTP Client-Server Implementation with Multiple Threads**

---

#### **Project Description**
https://github.com/user-attachments/assets/ff65c187-c1b4-4900-b5f9-49afc4ed8658

This project implements a simple FTP (File Transfer Protocol) client-server system using multiple threads to support concurrent file transfers. The system consists of two programs:
1. **ftpserver**: A server program that listens on a specified TCP port and handles multiple client connections using threads.
2. **ftpclient**: A client program that connects to the server and allows users to upload or download files.

The server and client programs support the following commands:
- **get <filename>**: Downloads a file from the server.
- **upload <filename>**: Uploads a file to the server.

Files are transferred in chunks of 1KB to handle large files efficiently. The server and client programs are designed to work on the same machine, with the server port specified as a command-line argument.



---

#### **Testing Sequence**
The execution sequence:
1. **Client 1** downloads `downloadTestFile1.jpg` from the server and saves it locally as `newDownloadTestFile1.jpg`.
2. **Client 2** downloads `downloadTestFile2.jpg` from the server and saves it locally as `newDownloadTestFile2.jpg`.
3. **Client 1** uploads `uploadTestFile1.jpg` to the server, which saves it as `newUploadTestFile1.jpg`.
4. **Client 2** uploads `uploadTestFile2.jpg` to the server, which saves it as `newUploadTestFile2.jpg`.

The file names are prefixed with "new" to avoid overwriting the original test files.

---

#### **Implementation Details**
1. **File Transfer**:
   - Files are split into 1KB chunks for transfer.
   - A loop is used to send/receive each chunk sequentially.
   - The end of the file transfer is signaled using a special marker or message.

2. **Concurrency**:
   - The server uses multiple threads to handle multiple clients simultaneously.
   - Each client connection is managed by a separate thread.

3. **Port Configuration**:
   - The default port for the server is **5106**.
   - If port 5106 is unavailable, you can choose another port number greater than 1024.

---

#### **How to Run the Programs**

1. **Start the Server**:
   - Compile the server program (if necessary).
   - Run the server with the following command:
     ```bash
     ./ftpserver 5106
     ```
   - Replace `5106` with another port number if needed.

2. **Start the Clients**:
   - Compile the client program (if necessary).
   - Run two instances of the client program in separate terminal windows:
     ```bash
     ./ftpclient 5106
     ```
   - Replace `5106` with the port number used by the server.

3. **Client Commands**:
   - To download a file:
     ```
     get downloadTestFile1.jpg
     ```
   - To upload a file:
     ```
     upload uploadTestFile1.jpg
     ```

---

#### **File Structure**
Place all files in the same directory:
- `ftpserver`: Server executable.
- `ftpclient`: Client executable.
- `downloadTestFile1.pptx`: Test file for download.
- `downloadTestFile2.pptx`: Test file for download.
- `uploadTestFile1.pptx`: Test file for upload.
- `uploadTestFile2.pptx`: Test file for upload.

---

#### **Output Files**
After testing, the following files will be created:
- `newDownloadTestFile1.pptx`: Downloaded by Client 1.
- `newDownloadTestFile2.pptx`: Downloaded by Client 2.
- `newUploadTestFile1.pptx`: Uploaded by Client 1.
- `newUploadTestFile2.pptx`: Uploaded by Client 2.

---

#### **Dependencies**
- The implementation is written in Python.
- 'socket', 'os', 'threading' libraries are used

---

#### **Notes**
- This implementation does not conform to the FTP standard.
- The server and client programs are designed for simplicity and educational purposes.

---
