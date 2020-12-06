import mysql.connector
import tkinter as tk
import PIL
from mysql.connector import Error
from tkinter import *
from PIL import ImageTk, Image
from asyncio.base_events import Server

class functionFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#999999")
        self.controller = controller
        self.currentButtons = []
        self.page_list = ["Server", "DwellsIn", "PlayerAccount", "Shop", "NPCQuest", "PlayerCharacter", "Item", "Location", "NPCDialogue", "NPC", "Mob"]
        self.page = self.page_list[0]
        
        self.text = tk.Text(self, bg="#888888", fg="#FFFFFF", highlightthickness=0, font=("Orbitron", 14))
        self.text.place(relx=.3, rely=0, relwidth=.68, relheight=.99, anchor=NW)
        self.scroller = Scrollbar(self, bg="#666666")
        self.scroller.place(relx=1, rely=0, relheight=.99, relwidth= .02, anchor=NE)
        self.scroller.config(command=self.text.yview())
        self.text.configure(yscrollcommand=self.scroller.set)
        
        back = tk.Button(self, text="back", command=self.retreat)
        back.place(relx=0.05, rely=.98, anchor=SW)
        exampleText = "The width of the 3-d borders around the entire perimeter of the trough, and also the width of the 3-d effects on the arrowheads and slider. Default is no border around the trough, and a 2-pixel border around the arrowheads and slider."
        self.text.insert(INSERT, exampleText)
    def set_page(self, func_page):
        self.page = func_page
        
        for B in self.currentButtons:
            B.destroy()
        self.currentButtons.clear()
        self.update_left()
    def update_left(self):
        print("updating")
        if (self.page == self.page_list[0]):
            print("Server Options defined")
            self.server_protocol()
        elif self.page == self.page_list[1]:
            self.dwells_in_protocol()
        elif self.page == self.page_list[2]:
            self.player_account_protocol()
        elif self.page == self.page_list[3]:
            self.shop_protocol()
        elif self.page == self.page_list[4]:
            self.NPC_quest_protocol()
        elif self.page == self.page_list[5]:
            self.player_character_protocol()
        elif self.page == self.page_list[6]:
            self.item_protocol()
        elif self.page == self.page_list[7]:
            self.location_protocol()
        elif self.page == self.page_list[8]:
            self.NPC_dialogue_protocol()
        elif self.page == self.page_list[9]:
            self.mob_protocol()
        elif self.page == self.page_list[10]:
            self.NPC_protocol()
        
    def server_protocol(self):
        test = tk.Button(self, text="server option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
#         print("End server_protocol")
    def testCommand(self):
        _msg = "you selected the test command"
        self.add_text(_msg)
       
    def dwells_in_protocol(self):
        test = tk.Button(self, text="dwells option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
#         print("End server_protocol")
    def player_account_protocol(self):
        test = tk.Button(self, text="p_account option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
    def shop_protocol(self):
        test = tk.Button(self, text="shop option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
    def NPC_quest_protocol(self):
        test = tk.Button(self, text="npc quest option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
    def player_character_protocol(self):
        test = tk.Button(self, text="character option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
    def item_protocol(self):
        test = tk.Button(self, text="item option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
    def location_protocol(self):
        test = tk.Button(self, text="location option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
    def NPC_dialogue_protocol(self):
        test = tk.Button(self, text="npc dialogue option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
    def mob_protocol(self):
        test = tk.Button(self, text="mob option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
    def NPC_protocol(self):
        test = tk.Button(self, text="NPC option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
        
        
    def add_text(self, _text):
        self.text.insert(INSERT, "\n\n" + _text)
        self.text.yview_moveto('1')
    
    def retreat(self):
        self.controller.show_frame("DUMMY")
        