import socket, threading

host = socket.gethostname()
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen()
clients = {}
addresses = {}
print('Имя вашего чата' , host)
print("Чат готов...")
serverRunning = True
def handle_client(conn):
    try:
        data = conn.recv(1024).decode('utf8')
        welcome = 'Добро пожаловать %s! Если вы когда-нибудь захотите выйти, введите {quit}, чтобы выйти.' % data
        conn.send(bytes(welcome, "utf8"))
        msg = "%s присоединился в чату" % data
        broadcast(bytes(msg, "utf8"))
        clients[conn] = data
        while True:
            found = False
            response = 'Человек онлайн\n'
            msg1 = conn.recv(1024) 

            if msg1 != bytes("{quit}", "utf8"):
                broadcast(msg1, data+": ")
            else:
                conn.send(bytes("{quit}", "utf8"))
                conn.close()
                del clients[conn]
                broadcast(bytes("%s вышел из чата." % data, "utf8"))
                break
    except:
        print("%s вышел из чата." % data)
def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


while True:
    conn,addr = s.accept()
    conn.send("Введите имя: ".encode("utf8"))
    print("%s:%s has connected." % addr)
    addresses[conn] = addr
    threading.Thread(target = handle_client, args = (conn,)).start()
