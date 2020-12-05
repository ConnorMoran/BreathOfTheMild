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

        wl1 = Image.open("IP.png")
        wl2 = wl1.resize((163,25), Image.ANTIALIAS)
        self.wrongLabel = ImageTk.PhotoImage(wl2)

        self.wrong_label = Label(self, bg="#323232", image=self.wrongLabel)
        self.wrong_label.photo = self.wrongLabel
        self.wrong_label.grid(row=2, column=1)
        
        self.controller = controller

        self.password = Entry(self)
        
        self.password.grid(row=0, column=1, pady=10)
        self.password.config(show='*')
        
        password_label = Label(self, bg="#666666", text="Enter MySQL Password: ")
        password_label.grid(row=0, column=0)
        
        cancel_button = Button(self, text="Cancel", command=self.cancel)
        cancel_button.grid(row=3, column=2, columnspan=2, padx=10)
        
        go_1 = Image.open("go.png")
        go_2 = go_1.resize((320,50), Image.ANTIALIAS)
        self.go_image = ImageTk.PhotoImage(go_2)
        self.go_button = Button(self, bg="#323232", image=self.go_image, borderwidth=0, command=self.create_connection)
        self.go_button.photo = self.go_image
        self.go_button.bind("<Enter>", self.go_enter)
        self.go_button.bind("<Leave>", self.go_exit)
        self.go_button.grid(row=4, column=0)
        
        go_p1 = Image.open("go_push.png")
        go_p2 = go_p1.resize((320,50), Image.ANTIALIAS)
        self.go_pimage = ImageTk.PhotoImage(go_p2)

        
        password_button = Button(self, text="Submit Password", command=self.create_connection)
        password_button.grid(row=3, column=0, columnspan=2)
        
#     def printer(self):
#        print("{} {}".format(self.i, self.j))
       
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
            self.controller.set_connection(connection)
            self.controller.show_frame("DUMMY")
            output_msg = "Connection to MySQL DB successful"
            print (output_msg)
        except Error as e:
            print(f"The error '{e}' occurred")
            
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