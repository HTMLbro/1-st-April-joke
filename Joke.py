import os
import time
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox

def shutdown_system():
    root.destroy()
    messagebox.showwarning("Shutdown", "Зараз ваш комп'ютер буде вимкнено через 10 секунд.")
    subprocess.call(["shutdown", "/s", "/t", "10"])
    time.sleep(5)
    subprocess.call(["shutdown", "/a"]) # Cancel the shutdown after 5 seconds
    messagebox.showinfo("Shutdown Cancelled", "Жартую! Гарного дня! :)")
    
root = tk.Tk()
root.title("Auto Shutdown")
root.geometry("25x25")

label = tk.Label(root, text="Програма-жарт на 1-ше квітня")
label.pack(pady=20)

shutdown_system()