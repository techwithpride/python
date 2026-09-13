import time
import tkinter as tk
root=tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.config(bg="purple")

label=tk.Label(root,font=("ds-digital",80),bg="purple",fg="cyan")
label.pack(anchor="center",expand=True)

def update_time():
    current_time=time.strftime("%H:%M:%S %p")
    label.config(text=current_time)
    label.after(1000,update_time)

update_time()
root.mainloop()