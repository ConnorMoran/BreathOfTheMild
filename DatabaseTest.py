import mysql.connector
import tkinter as tk
import login
from mysql.connector import Error

from tkinter import *
#CHANGE
#CHANGE2
# def create_connection():
#     global connection
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             passwd=password.get(),
#             database = "breathofthemild"
#         )
#         output_msg = "Connection to MySQL DB successful"
#     except Error as e:
#         print(f"The error '{e}' occurred")
#         root.destroy()
# 
#     password.destroy()
#     password_label.destroy()
#     password_button.destroy()
# 
#     menu_options = ["Insert", "Update", "Delete", "Display"]
#     selected = StringVar(root)
#     selected.set(menu_options[0])
#     menu = OptionMenu(root, selected, *menu_options, command=done)
#     menu.grid(row=0, column=0, pady=10)

    # location_fields = execute_read_query(connection, "SHOW COLUMNS FROM location")
    # for i in range(len(location_fields)):
    #     entry = Label(root, text=str(location_fields[i][0]))
    #     entry.grid(row=0, column=i)
    #
    # locations_table = execute_read_query(connection, "Select * from location")
    # table_contents = []
    # for i in range(len(locations_table)):
    #     for j in range(len(locations_table[i])):
    #         entry = Label(root, text=str(locations_table[i][j]))
    #         entry.grid(row=i+1, column=j)
    #         table_contents.append(entry)



# def execute_read_query(connection, query):
#     cursor = connection.cursor()
#     result = None
#     try:
#         cursor.execute(query)
#         result = cursor.fetchall()
#         return result
#     except Error as e:
#         print(f"The error '{e}' occurred")

# def done(selected):
#     print("Yay!")

# global connection
# root = Tk()
# root.title("Test Database")
# root.geometry("700x700")
# 
# password = Entry(root)
# password.grid(row=0, column=1, pady=10)
# password.config(show='*')
# 
# password_label = Label(root, text="Enter MySQL Password: ")
# password_label.grid(row=0, column=0)
# 
# password_button = Button(root, text="Submit Password", command=create_connection)
# password_button.grid(row=2, column=0, columnspan=2)

class MainFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
            
        self.frames = {}
        for F in (Index, login.loginFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.width = 500;
            frame.height = 500;
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("Index")
        
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class Index(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="BREATH OF THE MILD")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Admin Login",
                           command=lambda: controller.show_frame("loginFrame"))
        button.pack()
# canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# canvas.place(relwidth=0.9, relheight=0.9, relx=0.1, rely=0.1)
# canvas.pack()

# root = tk.Tk()
# root.title("Breath of the Mild")
# 
# mainPanel = login.login(root)
# loginFrame = mainPanel.get_frame()
# root.mainloop()
root = tk.Tk()
upperFrame = tk.Frame(root, width=500, height = 200, background="#999999")
upperFrame.place(relwidth=0.9, relheight=0.9, relx=0.1,rely=0.1)
mainFrame = MainFrame(root)
mainFrame.place(relx=.5, rely=.5)
if __name__ == "__main__":
    root.mainloop()

