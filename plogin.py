import mysql.connector
import tkinter as tk
import PIL
from mysql.connector import Error
from tkinter import *
from PIL import ImageTk, Image
import functions
import tkinter.font as tkFont
class ploginFrame(tk.Frame):
     
    global connection
    
    #initialize frame with parent frame and controller container. Allows MainFrame stacking
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#323232")
        self.controller = controller
        myStyle = tkFont.Font(family="Lucida Grande", size=20)
        #username Label:
        self.uLabel = Label(self, text="Username: ", font=myStyle)
        
        #password label
        self.pLabel = Label(self, text="Password: ", font=myStyle)
          
        
        #create incorrect password label
        wl1 = Image.open("IP.png")
        wl2 = wl1.resize((320,50), Image.ANTIALIAS)
        self.wrongLabel = ImageTk.PhotoImage(wl2)
        self.wrong_label = Label(self, bg="#323232", image=self.wrongLabel)

        #text entry for typing username in
        self.username = Entry(self)
        self.username.bind("<Key>", self.retype)
        
        
        #text entry for typing password in
        self.password = Entry(self)
        self.password.bind("<Key>", self.retype)
        self.password.config(show='*')
        
        #try to log-in button, takes you to [DatabaseSelection]
        go_1 = Image.open("go.png")
        go_2 = go_1.resize((240,38), Image.ANTIALIAS)
        self.go_image = ImageTk.PhotoImage(go_2)
        self.go_button = Label(self, image=self.go_image, bg="#323232")
        self.go_button.bind("<Enter>", self.go_enter)
        self.go_button.bind("<Button>", self.go_click)
        self.go_button.bind("<Return>", self.go_click)
        self.go_button.bind("<Leave>", self.go_exit)
        
        #cancel button, takes you back to Index
        c1 = Image.open("cancel.png")
        c2 = c1.resize((240,38), Image.ANTIALIAS)
        self.cancel_image = ImageTk.PhotoImage(c2)
        self.cancel_button = Label(self, image=self.cancel_image, bg="#323232")
        self.cancel_button.bind("<Enter>", self.c_enter)
        self.cancel_button.bind("<Button>", self.cancel_click)
        self.cancel_button.bind("<Leave>", self.c_exit)
        
        #image reference for mouse hover [login button]
        go_p1 = Image.open("go_push.png")
        go_p2 = go_p1.resize((240,38), Image.ANTIALIAS)
        self.go_pimage = ImageTk.PhotoImage(go_p2)
        
        #image reference for mouse hover [Cancel button]
        c_p1 = Image.open("cancelClick.png")
        c_p2 = c_p1.resize((240,38), Image.ANTIALIAS)
        self.c_pimage = ImageTk.PhotoImage(c_p2)
        
        self.init_state()
        
    #try to establish a connection given password
    def create_connection(self):
        global connection
        connection = None
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=self.password.get(),
                database = "breathofthemild"
            )
            self.controller.set_connection(connection)
            self.scene_change("DatabaseSelectionFrame")
            #delete later
            print (self.controller.get_current_frame())

        except Error as e:
            self.wrong_label.place(relx=.40, rely=.62, anchor=CENTER)
            
    def cancel(self):
        self.scene_change("IndexFrame")
        
    def go_enter(self, event):
        print("entering!")
        self.go_button.config(image=self.go_pimage)
    def go_exit(self, event):
        print("Exiting!")
        self.go_button.config(image=self.go_image)
    def c_enter(self, event):
        print("entering!")
        self.cancel_button.config(image=self.c_pimage)
    def c_exit(self, event):
        print("Exiting!")
        self.cancel_button.config(image=self.cancel_image)
        
    def retype(self, event):
        self.wrong_label.place_forget()

    def get_frame(self):
        return self.frame
        
    def go_click(self, x):
        
        users = self.execute_read_query(self.controller.get_connection(), "SELECT accountName FROM PlayerAccount WHERE accountName='" + self.username.get() + "';")
        if len(users) == 0:
            print("NO USERNAME MATCH")
            self.wrong_label.place(relx=.40, rely=.72, anchor=CENTER)
        else:
            print("USERNAME MATCH")
            password = self.execute_read_query(self.controller.get_connection(), "SELECT Password FROM PlayerAccount WHERE accountName='" + self.username.get() + "';")
            if len(password) ==0:
                print("Invalid Password")
                self.wrong_label.place(relx=.40, rely=.72, anchor=CENTER)
            else:
                print("PASSWORD MATCH")
                self.controller.show_account(self.username.get())
                self.init_state()
    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
            
    def cancel_click(self, x):
        self.cancel()
    #general scene changer. sets frame to its initial state and changes scene in MainFrame
    def scene_change(self, scene):
        self.controller.show_frame(scene)
        self.init_state()
    
    def init_state(self):
        self.wrong_label.place(relx=.40, rely=.62, anchor=CENTER)
        self.wrong_label.place_forget()
        
        self.uLabel.place(relx=.5, rely=.08, anchor=CENTER)
        self.username.place(relx=.5, rely=.14, anchor=CENTER)
        
        self.pLabel.place(relx=.5, rely=.26, anchor=CENTER)
        self.password.place(relx=.5, rely=.32, anchor=CENTER)
        
        self.go_button.place(relx=.7, rely=.90, anchor=CENTER)
        self.cancel_button.place(relx=.2, rely=.90, anchor=CENTER)
        self.password.delete(0, END)
        
        self.username.delete(0, END)
        
                