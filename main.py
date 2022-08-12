from vidstream import *
import tkinter as tk
import socket
import threading
import requests
import os 


local_ip_address = socket.gethostbyname(socket.gethostname())

server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)





def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()


def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'), 7777)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

def start_chat():
    os.system('python client.py')

def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0,'end-1c'), 6666)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()




# GUI

window = tk.Tk()
window.title("Lite Conferences v1.0 Alpha")
window.geometry('400x300')

label_target_ip = tk.Label(window, text="IP администратора :")
label_target_ip.pack()
text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()



btn_listen = tk.Button(window, text="Начать слушать", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Включить камеру", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Включить чат", width=50, command=start_chat)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Включить микро", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()
