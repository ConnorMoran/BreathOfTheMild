import mysql.connector
import tkinter as tk
import PIL
from mysql.connector import Error
from tkinter import *
from PIL import ImageTk, Image


class IndexFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#323232")
        self.controller = controller

#         tempImg = PIL.Image.open("Index.png")
#         background_image = ImageTk.PhotoImage(tempImg)
#         inLab = Label(self, image = background_image, bg="#323232").place(relwidth = 1, relheight=1, relx=0, rely=0)
        label = tk.Label(self, text="BREATH OF THE MILD")
        
        wl1 = Image.open("Index.png")
        wl2 = wl1.resize((700,500), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(wl2)
        self.bg_label = Label(self, bg="#323232", image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)
        
        #player button
        Pgo_1 = Image.open("player.png")
        Pgo_2 = Pgo_1.resize((130,20), Image.ANTIALIAS)
        self.Pgo_image = ImageTk.PhotoImage(Pgo_2)
        self.Pgo_button = Label(self, image=self.Pgo_image, bg="#a69b72", borderwidth=0)
        self.Pgo_button.bind("<Enter>", self.player_enter)
        self.Pgo_button.bind("<Button>", self.player_click)
        self.Pgo_button.bind("<Leave>", self.player_exit)
        
        #admin button
        Ago_1 = Image.open("Admin.png")
        Ago_2 = Ago_1.resize((130,20), Image.ANTIALIAS)
        self.Ago_image = ImageTk.PhotoImage(Ago_2)
        self.Ago_button = Label(self, image=self.Ago_image, bg="#a69b72", borderwidth=0)
        self.Ago_button.bind("<Enter>", self.admin_enter)
        self.Ago_button.bind("<Button>", self.admin_click)
        self.Ago_button.bind("<Leave>", self.admin_exit)
        
        
        
        #image reference for mouse hover [player button]
        go_p1 = Image.open("Player_hover.png")
        go_p2 = go_p1.resize((130,20), Image.ANTIALIAS)
        self.go_pimage = ImageTk.PhotoImage(go_p2)
        
        #image reference for mouse hover [Admin button]
        c_a1 = Image.open("Admin_hover.png")
        c_a2 = c_a1.resize((130,20), Image.ANTIALIAS)
        self.c_pimage = ImageTk.PhotoImage(c_a2)
        
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="Admin Login",
#                            command=lambda: controller.show_frame("loginFrame"))
#         button.pack()
        self.init_state()
        

    def player_enter(self, event):
        self.Pgo_button.config(image=self.go_pimage)
    def player_exit(self, event):
        self.Pgo_button.config(image=self.Pgo_image)
    def admin_enter(self, event):
        self.Ago_button.config(image=self.c_pimage)
    def admin_exit(self, event):
        self.Ago_button.config(image=self.Ago_image)
        
    def admin_click(self, e):
        self.controller.show_frame("DatabaseSelectionFrame")
    def player_click(self, e):
        self.controller.show_frame("ploginFrame")
        
    def init_state(self):
        self.Pgo_button.place(relx=.22, rely=.45)
        self.Ago_button.place(relx=.59, rely=.44)
        
        