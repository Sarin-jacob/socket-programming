def sender(filename,ip,port=1310):
    import socket
    import os
    filesize=os.path.getsize(filename)
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((ip,port))
        s.send(f"{filename}+{filesize}".encode())
        with open(filename,'rb') as f:
            while True:
                read=f.read(4096)
                if not read:
                    print(f"{os.path.basename(filename)} done transfering !")
                    s.close()
                    break
                s.sendall(read)
# sender('','')
sender('D:\Video\Can You Actually Game in 8K- (RTX 3090 Gameplay!) - YouTube.mp4','10.0.26.21')