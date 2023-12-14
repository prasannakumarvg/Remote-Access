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
                  >mkdir   - make directory
                  >cd ../  - go to previous directory
                  >hidden  - to show the hidden directories
                  >rm.file - remove a file
                  >rm.dir  - remove a directory
                  >file    - create a file
                  >open    - open a file
                  >copy    - to copy a file or directory
                  >move    - move a file or directory
                  >rename  - rename a file or directory
                  >exit    - exit the connectio
                  >help    - for the menu
                  """)
           while True:
             command = input("Enter Command : ")
             conn.send(command.encode())
    

             if command.lower() == "exit":
                break
             elif command.lower()=="mkdir":
                dire=str(input("Enter the directory : "))
                conn.send(dire.encode())
                data = conn.recv(1024)
                print(data.decode())
                continue

             elif command.lower() =="rm.file":
                file=str(input("Enter the filename : "))
                conn.send(file.encode())
                data = conn.recv(1024)
                print(data.decode())
                continue

             elif command.lower() =="rm.dir":
                file=str(input("Enter the filename : "))
                conn.send(file.encode())
                data = conn.recv(1024)
                print(data.decode())
                continue

             elif command.lower()=="cd":
                change=str(input("Enter the directory : "))
                conn.send(change.encode())
                data=conn.recv(1024)
                print(data.decode())
                continue
                
             elif command.lower()=="file":
                file=str(input("Enter the file name : "))
                conn.send(file.encode())
                data=conn.recv(1024)
                print(data.decode())
                continue
            

             elif command.lower() == "hidden":
                data = conn.recv(1024)
                result = json.loads(data.decode())
                print("Response from client:")
                for item in result:
                     print(item) 
                continue

             elif command.lower()=="copy":
                src=str(input("Enter the source : "))
                conn.send(src.encode())
                des=str(input("Enter the destination : "))
                conn.send(des.encode())
                data=conn.recv(1024)
                print(data.decode())
                continue
              
             elif command.lower()=="move":
                src=str(input("Enter the source : "))
                conn.send(src.encode())
                des=str(input("Enter the destination : "))
                conn.send(des.encode())
                data=conn.recv(1024)
                print(data.decode())
                continue

             elif command.lower()=="open":
                file=str(input("Enter the File Name : "))
                conn.send(file.encode())
                data=conn.recv(1024)
                print(data.decode())
                continue

             elif command.lower()=="rename":
                src=str(input("Enter the File name : "))
                conn.send(src.encode())
                des=str(input("Enter the New File name : "))
                conn.send(des.encode())
                data=conn.recv(1024)
                print(data.decode())
                continue

             elif command.lower()=="help":
                data=conn.recv(1024)
                print("""
                  >ls      - list the directories
                  >cd      - change the directories
                  >mkdir   - make directory
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
                continue

             else:
                data = conn.recv(1024)
                print( data.decode(),"\n")

       
        except KeyboardInterrupt:
               print("Server interrupted. Closing connection.")
        finally:
           if s.fileno() != -1:
               s.close()


if __name__ == '__main__':
    Main()
