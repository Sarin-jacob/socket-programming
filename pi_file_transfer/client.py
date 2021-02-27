def sender(filename,ip,port=1310):
    import socket
    import os
    filesize=os.path.getsize(filename)
    k=0
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        while k==0:
            s.connect((ip,port))
            s.send(f"{filename}+{filesize}".encode())
            with open(filename,'rb') as f:
                while True:
                    read=f.read(4096)
                    if not read:
                        print(f"{os.path.basename(filename)} done transfering !")
                        k=1
                        s.close()
                        break
                    s.sendall(read)
sender('file','ip')