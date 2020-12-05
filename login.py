import mysql.connector
import tkinter as tk
import PIL
from mysql.connector import Error
from tkinter import *

from PIL import ImageTk, Image

class loginFrame(tk.Frame):
     
    global connection

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#323232")
        
        pl1 = Image.open("pwordLabel.png")
        pl2 = pl1.resize((320,50), Image.ANTIALIAS)
        self.pl = ImageTk.PhotoImage(pl2)
        self.pLabel = Label(self, bg="#323232", image=self.pl)
        self.pLabel.photo = self.pl
        self.pLabel.place(relx=.3, rely=.08)
        
        
        wl1 = Image.open("IP.png")
        wl2 = wl1.resize((320,50), Image.ANTIALIAS)
        self.wrongLabel = ImageTk.PhotoImage(wl2)
        self.wrong_label = Label(self, bg="#323232", image=self.wrongLabel)
        self.wrong_label.photo = self.wrongLabel
        self.wrong_label.place(relx=.35, rely=.24)
        self.wrong_label.place_forget()
        self.controller = controller

        self.password = Entry(self)
        self.password.bind("<Key>", self.retype)
        self.password.place(relx=.4, rely=.25)
        self.password.config(show='*')
               
        go_1 = Image.open("go.png")
        go_2 = go_1.resize((320,50), Image.ANTIALIAS)
        self.go_image = ImageTk.PhotoImage(go_2)
        self.go_button = Button(self, image=self.go_image, borderwidth=0, command=self.create_connection)
        self.go_button.photo = self.go_image
        self.go_button.bind("<Enter>", self.go_enter)
        self.go_button.bind("<Leave>", self.go_exit)
        self.go_button.place(relx=.05, rely=.72)
        
        c1 = Image.open("cancel.png")
        c2 = c1.resize((320,50), Image.ANTIALIAS)
        self.cancel_image = ImageTk.PhotoImage(c2)
        self.cancel_button = Button(self, image=self.cancel_image, borderwidth=0, command=self.cancel)
        self.cancel_button.photo = self.cancel_image
        self.cancel_button.bind("<Enter>", self.c_enter)
        self.cancel_button.bind("<Leave>", self.c_exit)
        self.cancel_button.place(relx=.50, rely=.72)
        
        go_p1 = Image.open("go_push.png")
        go_p2 = go_p1.resize((320,50), Image.ANTIALIAS)
        self.go_pimage = ImageTk.PhotoImage(go_p2)
        
        c_p1 = Image.open("cancelClick.png")
        c_p2 = c_p1.resize((320,50), Image.ANTIALIAS)
        self.c_pimage = ImageTk.PhotoImage(c_p2)
        
       
    def create_connection(self):
        global connection
        connection = None
        self.test_dimension()
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=self.password.get(),
                database = "breathofthemild"
            )
            self.password.delete()
            self.controller.set_connection(connection)
            self.controller.show_frame("DUMMY")
            output_msg = "Connection to MySQL DB successful"
            print (output_msg)
        except Error as e:
            print(f"The error '{e}' occurred")
            self.wrong_label.place(relx=.3, rely=.36)
            
    def cancel(self):
        self.controller.show_frame("Index")
        print("cancelling..")
        print(self.wrong_label.size())
    def go_enter(self, event):
        print("entering!")
        self.go_button.config(image=self.go_pimage)
        self.go_button.image = self.go_pimage
    def go_exit(self, event):
        print("Exiting!")
        self.go_button.config(image=self.go_image)
        self.go_button.image = self.go_image
    def c_enter(self, event):
        print("entering!")
        self.cancel_button.config(image=self.c_pimage)
        self.cancel_button.image = self.c_pimage
    def c_exit(self, event):
        print("Exiting!")
        self.cancel_button.config(image=self.cancel_image)
        self.cancel_button.image = self.cancel_image
        
    def retype(self, event):
        self.wrong_label.place_forget()
    
    def execute_read_query(connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
    
    def get_frame(self):
        return self.frame
        
    def done(selected):
        print("Yay!")
        
    def test_dimension(self):
        print(self.controller.size)
        
#         menu_options = ["Insert", "Update", "Delete", "Display"]
#         selected = StringVar(frame)
#         selected.set(menu_options[0])
#         menu = OptionMenu(frame, selected, *menu_options, command=done)
#         menu.grid(row=0, column=0, pady=10)