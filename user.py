import socket
import os
import subprocess
import json
import shutil

def Main():
    s = socket.socket()
    host = str(input("Enter the IP address: "))
    port = 8080

    s.connect((host, port))
    print("Connected to Server.")
    try:
      while True:
        command = s.recv(1024).decode()

        if command.lower() == "exit":
            print("Connection closed by server.")
            break

        elif command.lower() == "ls":
            result = os.popen('ls').read()
            s.send(result.encode())

        elif command.lower() == "hidden":
            result = [item for item in os.listdir('.') if item.startswith('.')]
            resultj=json.dumps(result)
            s.send(resultj.encode())


        elif command.lower() == "cd ../":
            os.chdir("../")
            result = "Directory changed successfully."
            s.send(result.encode())

        elif command.lower() == "rm.file":
            file = s.recv(1024).decode()
            os.remove(file)
            result = f"File '{file}' deleted successfully."
            s.send(result.encode())

        elif command.lower() == "cwd":
            result = os.getcwd()
            s.send(result.encode())

        elif command.lower() == "mkdir":
            dire = s.recv(1024).decode()
            os.makedirs(os.path.join(os.path.expanduser("~"), dire), exist_ok=True)
            result = f"Directory '{dire}' created successfully."
            s.send(result.encode())

        elif command.lower() == "cd":
            change = s.recv(1024).decode()
            os.chdir(change)
            result = f"Directory '{change}' changed Successfully."
            s.send(result.encode())


        elif command.lower() == "rm.dir":
            directory = s.recv(1024).decode()
            shutil.rmtree(directory)
            result = f"Directory '{directory}' deleted successfully."
            s.send(result.encode())

        elif command.lower()== "file":
            name = s.recv(1024).decode()
            open(name, 'w')
            result = "File created sucessfully."
            s.send(result.encode())

        elif command.lower() == "copy":
            src = s.recv(1024).decode()
            des = s.recv(1024).decode()
            shutil.copy(src, des)
            result = "File copied sucessfully. "
            s.send(result.encode())
            
        elif command.lower() == "move":
            src = s.recv(1024).decode()
            des = s.recv(1024).decode()
            shutil.move(src, des)
            result = "File moved sucessfully. "
            s.send(result.encode())
        
        elif command.lower()=="open":
            file = s.recv(1024).decode()
            file_path = os.path.abspath(file)
            subprocess.run(["xdg-open", file_path], check=True)
            result = "Opened Sucessfully."
            s.send(result.encode())

        elif command.lower()=="rename":
            src = s.recv(1024).decode()
            des = s.recv(1024).decode()
            os.rename(src, des)
            result = "Name changed Successfully. "
            s.send(result.encode())
        
        elif command.lower()=="help":
             result="Empty"
             s.send(result.encode())

        else:
            result="Invalid Input "
            s.send(result.encode())

    
    
    except KeyboardInterrupt:
        print("Server interrupted. Closing connection.")

    finally:
        s.send(result.encode())


if __name__ == '__main__':
    Main()
