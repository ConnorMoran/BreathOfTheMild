import mysql.connector
import tkinter as tk
import PIL
from mysql.connector import Error
from tkinter import *
from PIL import ImageTk, Image


class accountFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#323232")
        self.controller = controller
        self.username = ""
#         tempImg = PIL.Image.open("Index.png")
#         background_image = ImageTk.PhotoImage(tempImg)
#         inLab = Label(self, image = background_image, bg="#323232").place(relwidth = 1, relheight=1, relx=0, rely=0)
        label = tk.Label(self, text="BREATH OF THE MILD")
        self.user = tk.Label(self, text="Currently signed in as: " + self.username)
        self.user.place(relx=.65, rely=.1)
        
        self.init_state()
        

    def player_enter(self, event):
        self.Pgo_button.config(image=self.go_pimage)
    def player_exit(self, event):
        self.Pgo_button.config(image=self.Pgo_image)
    def admin_enter(self, event):
        self.Ago_button.config(image=self.c_pimage)
    def admin_exit(self, event):
        self.Ago_button.config(image=self.Ago_image)
    def account_update(self, username):
        self.username = username;
        self.user.config(text="Currently signed in as: " + username)
        print(username)
    def admin_click(self, e):
        self.controller.show_frame("DatabaseSelectionFrame")
    def player_click(self, e):
        self.controller.show_frame("ploginFrame")
        
    def init_state(self):
        print ("initializing account page")
#         self.Pgo_button.place(relx=.22, rely=.45)
#         self.Ago_button.place(relx=.59, rely=.44)
        
        