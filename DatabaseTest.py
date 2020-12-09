import mysql.connector
import tkinter as tk
import login
import Index
import functions
import DatabaseEdit
import DatabaseSelection
import PIL
from PIL import ImageTk, Image
from mysql.connector import Error
from tkinter import *
#CHANGE
#CHANGE2
class MainFrame(tk.Frame):
   
    def __init__(self, parent):
        self._connection = None
        tk.Frame.__init__(self, parent, bg="#666666", width=500, height=500)
        container = tk.Frame(self)
        container.place(relwidth = .98, relheight = .98, relx=.01, rely=.01)
#         container.pack(expand=True)
        
        self.frames = {}
        for F in (Index.IndexFrame, login.loginFrame, DUMMY, functions.functionFrame, DatabaseEdit.DatabaseEditFrame, DatabaseSelection.DatabaseSelectionFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)

            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)
        self.show_frame("IndexFrame")
        self.current_frame = self.frames["IndexFrame"]
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if (page_name == "DUMMY"):
            frame.check_connection()
        if page_name == "DatabaseEditFrame":
            frame.create_table()
        if page_name == "DatabaseSelectionFrame":
            frame.create_buttons()
        frame.tkraise()
        self.current_frame = frame
        print(self.current_frame)
    def get_current_frame(self):
        return self.current_frame
    def set_connection(self, connection):
        self._connection = connection
        print(self._connection)
    def get_connection(self):
        return self._connection
    def set_current_table(self, table_name):
        self._current_table = table_name

    def get_current_table(self):
        return self._current_table
    def get_function_Frame(self):
        return self.frames["functionFrame"]
        
class DUMMY(tk.Frame):
    #example: this is where password screen takes you
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self._CONNECT = self.controller.get_connection()
       
        label = tk.Label(self, text="DUMMY")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back Home",
                           command=lambda: controller.show_frame("Index"))
        button.pack()
        
    def check_connection(self):
        print(self._CONNECT)
        print(self.controller.get_connection())

root = tk.Tk()
root.geometry("700x500+500+300")
root.resizable(0, 0)
root.title("Breath of the Mild")
# root.wm_attributes("-transparentcolor",'#333333')
# root.wm_attributes("-transparentcolor", 'grey')
upperFrame = tk.Frame(root, background="#999999")

logo = PIL.Image.open("logo.png")
logo2 = logo.resize((700,180), PIL.Image.ANTIALIAS)
logoImage = ImageTk.PhotoImage(logo2)
logoLabel = Label(upperFrame, bg="#999999", image=logoImage)
logoLabel.photo = logoImage
logoLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


upperFrame.place(relwidth=1, relheight=0.3)
mainFrame = MainFrame(root)

mainFrame.place(relwidth = 1, relheight = .7, relx=0, rely=.3)
if __name__ == "__main__":
    root.mainloop()
    
    
    
    
#     def execute_read_query(connection, query):
#         cursor = connection.cursor()
#         result = None
#         try:
#             cursor.execute(query)
#             result = cursor.fetchall()
#             return result
#         except Error as e:
#             print(f"The error '{e}' occurred")

#         menu_options = ["Insert", "Update", "Delete", "Display"]
#         selected = StringVar(frame)
#         selected.set(menu_options[0])
#         menu = OptionMenu(frame, selected, *menu_options, command=done)
#         menu.grid(row=0, column=0, pady=10)