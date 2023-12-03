import socket
import sys
import json

def Main():
    s = socket.socket()
    host = socket.gethostname()
    port = 8080
    print("""
        
██████╗░███████╗███╗░░░███╗░█████╗░████████╗███████╗  ░█████╗░░█████╗░░█████╗░███████╗░██████╗░██████╗
██╔══██╗██╔════╝████╗░████║██╔══██╗╚══██╔══╝██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
██████╔╝█████╗░░██╔████╔██║██║░░██║░░░██║░░░█████╗░░  ███████║██║░░╚═╝██║░░╚═╝█████╗░░╚█████╗░╚█████╗░
██╔══██╗██╔══╝░░██║╚██╔╝██║██║░░██║░░░██║░░░██╔══╝░░  ██╔══██║██║░░██╗██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗
██║░░██║███████╗██║░╚═╝░██║╚█████╔╝░░░██║░░░███████╗  ██║░░██║╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝  ╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░
                                                                                                                                  
        """)
                                                                                        

    s.bind(('0.0.0.0', port))
    print("Hostname:", host)
    print("Waiting for connections...")

    while True:
        s.listen()
        try:
           conn, addr = s.accept()
           print(addr, "is connected to the server")
           print("""
                  >ls      - list the directories
                  >cd      - change the directories
                  >cd ../  - go to previous directory
                  >hidden  - to show the hidden directories
                  >rm.file - remove a file
                  >rm.dir  - remove a directory
                  >file    - create a file
                  >open    - open a file
                  >copy    - to copy a file or directory
                  >move    - move a file or directory
                  >rename  - rename a file or directory
                  >exit    - exit the connection
                  """)
           while True:
             command = input("Enter Command : ")
             conn.send(command.encode())
    

             if command.lower() == "exit":
                break
             if command.lower()=="mkdir":
                dire=str(input("Enter the directory : "))
                conn.send(dire.encode())
                data = conn.recv(1024)
                print(data.decode())
                continue

             if command.lower() =="rm.file":
                file=str(input("Enter the filename : "))
                conn.send(file.encode())
                data = conn.recv(1024)
                print(data.decode())
                continue

             if command.lower() =="rm.dir":
                file=str(input("Enter the filename : "))
                conn.send(file.encode())
                data = conn.recv(1024)
                print(data.decode())
                continue

             if command.lower()=="cd":
                change=str(input("Enter the directory : "))
                conn.send(change.encode())
                data=conn.recv(1024)
                print(data.decode())
                continue
                
             if command.lower()=="file":
                file=str(input("Enter the file name : "))
                conn.send(file.encode())
                data=conn.recv(1024)
                print(data.decode())
                continue
            

             if command.lower() == "hidden":
                data = conn.recv(1024)
                print("Received data : ",data.decode())
                result = json.loads(data.decode())
                print("Response from client:")
                for item in result:
                     print(item) 
                continue

             if command.lower()=="copy":
                src=str(input("Enter the source : "))
                conn.send(src.encode())
                des=str(input("Enter the destination : "))
                conn.send(des.encode())
                data=conn.recv(1024)
                print(data.decode())
                continue
              
             if command.lower()=="move":
                src=str(input("Enter the source : "))
                conn.send(src.encode())
                des=str(input("Enter the destination : "))
                conn.send(des.encode())
                data=conn.recv(1024)
                print(data.decode())
                continue

             if command.lower()=="open":
                file=str(input("Enter the File Name : "))
                conn.send(file.encode())
                data=conn.recv(1024)
                print(data.decode())
                continue

             if command.lower()=="rename":
                src=str(input("Enter the File name : "))
                conn.send(src.encode())
                des=str(input("Enter the New File name : "))
                conn.send(des.encode())
                data=conn.recv(1024)
                print(data.decode())
                continue

             data = conn.recv(1024)

             if data:
                print("Response from client :  ", data.decode(),"\n")

       
        except KeyboardInterrupt:
               print("Server interrupted. Closing connection.")
        finally:
           if s.fileno() != -1:
               s.close()


if __name__ == '__main__':
    Main()
