def reciever(port=1310):   
    import socket
    import tqdm
    import os
    host=socket.gethostbyname(socket.gethostname())
    host1='0.0.0.0'
    print('\n',host,'is the servers pi address',end='\n\n')
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((host1,port))
        s.listen(5)
        print(f" Listening as {host} : {port}")
        conn,addr =s.accept()  
        print(f'{addr} is connected !')
        data=conn.recv(4096).decode()
        filename,filesize=data.split('+')
        filename=os.path.basename(filename)
        filesize=int(filesize)
        progress=tqdm.tqdm(range(filesize),f'Receiving {filename}',unit='B',unit_scale=True,unit_divisor=1024)
        with open(filename,'wb') as f:
            while True:
                read=conn.recv(4096)
                if not read:
                    conn.close()
                    break
                f.write(read)
                progress.update(len(read))
            print(f'\n {filename} done receiving !')
while True:
    reciever()
