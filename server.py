# https://www.biob.in/2018/04/simple-server-and-client-chat-using.html
# https://realpython.com/python-sockets/

import time, socket, os
    
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1919

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    os.system('cls')
    print("\nChat Room\n")
    time.sleep(1)
    print("Hostname:", host)
    print("IP address:", ip)
    print("Port:", port)
    s.listen()
    print("Waiting for connection...")
    conn, addr = s.accept()     
    print("Received connection from ", addr[0], "(", addr[1], ")\n")
    time.sleep(1)
    os.system('cls')
    print("Waiting for client message...")
    while True:
        message = conn.recv(1024)
        message = message.decode()
        if message == "/q":
            break
        print("Client:", message)
        message = input(str("> : "))
        conn.send(message.encode())
