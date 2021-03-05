def sender(filename,ip,port=1310):
    import socket
    import os
    import errno
    if '<<=>>' in filename: #used so that '<<=>>' can still be used as seperator !
        print('changing file name !. \n"<<=>>" should not be there in filename. \nfilename changed.')
        os.rename(f'{filename}',f'{filename.replace("<<=>>","_")}')
        filename=filename.replace('<<=>>','_')
    filesize=os.path.getsize(filename)
    k=0
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        while k==0:
            try:
                s.connect((ip,port))
                s.send(f"{filename}<<=>>{filesize}".encode())
                with open(filename,'rb') as f:
                    while True:
                        read=f.read(4096)
                        if not read:
                            print(f"{os.path.basename(filename)} done transfering !")
                            k=1
                            s.close
                            break
                        s.sendall(read)
            except Exception as e:
            	if e.errno==9:
            		k=1
            		print('file not sent')
            	s.close
            	continue
sender('file','ip')