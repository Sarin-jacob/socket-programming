def filez(conn,addr):#trial3
    import socket
    import tqdm
    import os
    from time import ctime ,sleep
    try:
        print(f'{addr} is connected !')
        with open('receiver_log.txt','a') as log:
                log.write(f'\nTime :{ctime()} -> {addr} is connected !')
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
            # sleep(10)
            print(f'\n {filename} done receiving !')
            with open('receiver_log.txt','a') as log:
                if filesize-int(os.path.getsize(filename))<=(filesize/100):
                    log.write(f"\nTime :{ctime()} -> {filename} ({filesize}B) received from {addr}")
                else:
                    log.write(f"\nTime :{ctime()} -> {filename} ({filesize}B) received from {addr} is 'broken'")
    except Exception as e:
        with open('receiver_log.txt','a') as log:
            log.write(f'\nTime :{ctime()} -> {e}')
        conn.close()
def reciever(port=1310):  
    import socket
    import tqdm
    import os
    from time import ctime
    from _thread import start_new_thread
    with open('receiver_log.txt','a') as log:
            log.write(f'\n###############################################################################\n\nTime :{ctime()} -> Reciever have started!\n')
    host=socket.gethostbyname(socket.gethostname())
    host1='0.0.0.0'
    print('\n',host,'is the servers pi address',end='\n\n')
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((host1,port))
        s.listen(5)
        print(f" Listening as {host} : {port}")
        while True:       
            conn,addr =s.accept()
            start_new_thread(filez,(conn,addr)) 
        
        
reciever()
