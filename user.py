import socket
import os
import shutil

def Main():
    s = socket.socket()
    host = str(input("Enter the IP address: "))
    port = 8080

    s.connect((host, port))
    print("Connected to Server.")

    while True:
        command = s.recv(1024).decode()

        if command.lower() == "exit":
            print("Connection closed by server.")
            break

        if command.lower() == "ls":
            result = os.popen('ls').read()
            s.send(result.encode())

        if command.lower() == "cd ../":
            os.chdir("../")
            result = "Directory changed successfully."
            s.send(result.encode())

        if command.lower() == "rm.file":
            file = s.recv(1024).decode()
            os.remove(file)
            result = f"File '{file}' deleted successfully."
            s.send(result.encode())

        if command.lower() == "cwd":
            result = os.getcwd()
            s.send(result.encode())

        if command.lower() == "mkdir":
            dire = s.recv(1024).decode()
            os.makedirs(os.path.join(os.path.expanduser("~"), dire), exist_ok=True)
            result = f"Directory '{dire}' created successfully."
            s.send(result.encode())

        if command.lower() == "cd":
            change = s.recv(1024).decode()
            os.chdir(change)
            result = f"Directory '{change}' changed Successfully."
            s.send(result.encode())

        if command.lower() == "rm.dir":
            directory = s.recv(1024).decode()
            shutil.rmtree(directory)
            result = f"Directory '{directory}' deleted successfully."
            s.send(result.encode())

        if command.lower() == "file":
            name = s.recv(1024).decode()
            open(name, 'w').close()  # Create an empty file
            result = f"File '{name}' created successfully."
            s.send(result.encode())

if __name__ == '__main__':
    Main()

