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

        label = tk.Label(self, text="BREATH OF THE MILD")

        self.user = tk.Label(self, text="Currently signed in as: " + self.username)
        self.user.place(relx=.65, rely=.1)
        self.characters = tk.Label(self, text="My Characters: ")
        self.characters.place(relx=.05, rely=.0)
        self.logout = tk.Button(self, text="Log Out", command = self.log)
        self.logout.place(relx=.03, rely=.9)
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
        
        query = "select characterName,Level FROM PlayerCharacter WHERE AccountName='" + username + "';"
        charList = self.execute_read_query(self.controller.get_connection(), query)
        counter = 1
        for ch in charList:
            counter = counter + 1
            lab = tk.Label(self, text="--Character Name: " + ch[0] + " Level: " + str(ch[1]))
            lab.place(relx=.05, rely = .05 + (counter * .05))
        
    def admin_click(self, e):
        self.controller.show_frame("DatabaseSelectionFrame")
    def player_click(self, e):
        self.controller.show_frame("ploginFrame")
        
    def log(self):
        self.controller.show_frame("IndexFrame")
    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")     
            
            
            
            
            
            
            
            
            
#             IN INIT:
#         back_button = Button(self, text="back..", command=lambda: self.controller.show_frame("DatabaseSelectionFrame"))
#         back_button.grid(row=10, column=0)
        