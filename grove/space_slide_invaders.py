#!/bin/usr/env python

from tkinter import *
import grove_client

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.distance_label = Label(text="Distance")
        self.distance_label.place(x=50,y=50)

    def set_client(self, client):
        self.client = client

    def update_distance(self):
        distance = self.client.get_distance()
        print(distance)
        self.distance_label.configure(text=str(distance))
        self.after(100, self.update_distance)

root = Tk()
app = App(root)

try:
    client = grove_client.GroveClient()
    app.set_client(client)
    app.update_distance()
except:
    print("Client connection could not be established")

root.wm_title("Space Slide Invaders")
root.geometry("500x200")
root.mainloop()

