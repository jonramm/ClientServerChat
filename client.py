import time, socket, os

host = "192.168.0.27"
port = 1919

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    os.system('cls')
    print("\nChat Room\n")
    time.sleep(1)
    print("Waiting to connect...")
    s.connect((host, port))
    print("Connected to", host ,"\n")
    time.sleep(1)
    print("Please enter a message...")
    while True:
        message = input(str("> : "))
        if message == "/q":
            s.send(message.encode())
            break
        s.send(message.encode())
        message = s.recv(1024)
        message = message.decode()
        print("Server: ", message)
