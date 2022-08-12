import socket,threading,tkinter
host = input("Введите имя чата: ")
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (host,port)
def echo_data(sock):
   while True:
      try:
         msg = sock.recv(1024).decode('utf8')
         msg_list.insert(tkinter.END, msg)
      except OSError:
         break



def send(event=None):
   msg = my_msg.get() 
   my_msg.set("")
   s.send(bytes(msg, "utf8"))
   if msg == "{quit}":
      s.close()
      top.quit()


def on_closing(event=None):
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Чат комнаты")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  
my_msg.set(".")
scrollbar = tkinter.Scrollbar(messages_frame)  
msg_list = tkinter.Listbox(messages_frame, height=15, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

address = (host,port)
s.connect(address)

threading.Thread(target=echo_data, args = (s,)).start()

tkinter.mainloop()
