
import mysql.connector
import tkinter as tk
from mysql.connector import Error
from tkinter import *
from functools import partial


class DatabaseSelectionFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#323232")
        back = tk.Button(self, text="Back", command=self.back)
        back.place(relx=.02, rely=.95)
        self.controller = controller
        self.tables = []
        self.error = Label(self, text="")

    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
            self.error.config(text=f"The error '{e}' occurred")

    def create_buttons(self):
        if self.controller.get_connection() is not None:

            table_names = self.execute_read_query(self.controller.get_connection(), "Show Tables")
            self.tables = []
            for name in table_names:
                self.tables.append(name[0])

            for i, name in enumerate(self.tables):
                button = Button(self, text=name, command=partial(self.select_table, i))
                button.place(relx=0.4, rely=i*0.07+0.05, anchor=CENTER)

    def select_table(self, num):
        self.controller.set_current_table(self.tables[num])
        self.controller.show_frame("DatabaseEditFrame")
    
    def back(self):
        self.controller.show_frame("IndexFrame")