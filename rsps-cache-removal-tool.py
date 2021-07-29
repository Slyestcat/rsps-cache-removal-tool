from random import randint
from threading import Thread
from tkinter import Tk, DoubleVar, HORIZONTAL, messagebox, Label, LEFT
from tkinter.ttk import Frame, Button, Progressbar
from time import sleep
import shutil
import os
from pathlib import Path
import psutil
import webbrowser


class Worker(Thread):
    def __init__(self, reference):
        super().__init__()
        self.reference = reference

    def run(self):
        home = str(Path.home())
        directory = "#" #insert cache folder name here
        path = os.path.join(home, directory)
        for proc in psutil.process_iter():
            if any(procstr in proc.name() for procstr in\
                ['javaw']):
                print(f'Killing {proc.name()}')
                proc.kill()
        self.reference.add_progress(40)
        sleep (4.0)
        self.reference.add_progress(20)
        sleep (4.0)
        self.reference.add_progress(20)
        sleep (4.0)
        self.reference.add_progress(20)
        sleep (4.0)
        self.reference.add_progress(20)
        sleep (4.0)
        self.reference.add_progress(20)
        shutil.rmtree(path)
        self.reference.add_progress(60)

class Example(Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.label = Label(root, text = "Cache Removal Tool")
        self.label.config(font = ("Arial", 14))
        self.label.pack(pady=10)
        self.progress = DoubleVar(value=0.0)
        self.worker = Worker(reference=self)
        self.progressbar = Progressbar(master=self, orient=HORIZONTAL, length=200, mode='determinate', variable=self.progress)
        self.progressbar.pack()
        self.startbutton = Button(master=self, text="Start", command=self.start)
        self.startbutton.pack(side=LEFT, pady=4)
        self.infobutton = Button(master=self, text="Info", command=self.info)
        self.infobutton.pack(side=LEFT, pady=4)
        self.websitebutton = Button(master=self, text="Website", command=self.website)
        self.websitebutton.pack(side=LEFT, pady=4)
        self.pack()

    def get_progress(self):
        return self.progress.get()

    def set_progress(self, value):
        self.progress.set(value)

    def add_progress(self, value):
        self.progress.set(self.progress.get() + value)

    def start(self):
        home = str(Path.home())
        directory = "#" #insert cache folder name here
        path = os.path.join(home, directory)
        if os.path.exists(path):
            self.worker.start()
        else:
            messagebox.showinfo("Error","Cache doesn't exist")

    def info(self):
        messagebox.showinfo("Information","This program is designed to clear the rsps cache files.")

    def website(self):
        webbrowser.open('#', new=2)


def main():
    root = Tk()
    root.title("Cache Removal Tool")
    root.iconbitmap("#")
    root.geometry("300x120")
    root.resizable(0, 0)
    app = Example(root)
    app.mainloop()

if __name__ == '__main__':
    main()
