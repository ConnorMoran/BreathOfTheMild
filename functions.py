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
        elif self.page == self.page_list[10]:
            self.mob_protocol()
        elif self.page == self.page_list[9]:
            self.NPC_protocol()
        

        
#         print("End server_protocol")
    def characters_in_given_server(self):
        _msg = self.execute_read_query(self.controller.get_connection(), "SELECT charactername, ServerID FROM playercharacter WHERE ServerID = 1;")
        tempList = []
        for m in _msg:
            tempList.append(m[0])
        for mn in tempList:
            self.add_text(mn)
        self.add_text("------------------------------------------------------") 
    def mobs_in_location(self):
        _msg = self.execute_read_query(self.controller.get_connection(), "Select mobid, type From mob Where locationID=01 ORDER BY type")
        tempList = []
        for m in _msg:
            tempList.append(m)
        for mn in tempList:
            self.add_text(str(mn[0]) + str(mn[1]))
        self.add_text("------------------------------------------------------") 
    #error
    def shop_items(self):
        _msg = self.execute_read_query(self.controller.get_connection(), "SELECT Shop, Shopid From Shops Where shopid= 001")
        tempList = []
        for m in _msg:
            tempList.append(m)
        for mn in tempList:
            self.add_text(mn[0] + mn[1]) 
        self.add_text("------------------------------------------------------") 
    def npc_dialogue(self):
        _msg = self.execute_read_query(self.controller.get_connection(), "Select dialogue From Npcdialogue Where npcid = 01")
        tempList = []
        for m in _msg:
            tempList.append(m)
        for mn in tempList:
            self.add_text(mn[0]) 
        self.add_text("------------------------------------------------------") 
    def locations_in_a_server(self):
        _msg = self.execute_read_query(self.controller.get_connection(), "Select locationid From location Where serverid = 01")
        tempList = []
        for m in _msg:
            tempList.append(m)
        for mn in tempList:
            self.add_text(mn[0])         
        self.add_text("------------------------------------------------------") 
    def display_characters_items(self):
        _msg = self.execute_read_query(self.controller.get_connection(), "select ItemName from item where CharacterName = 'George';")
        tempList = []
        for m in _msg:
            tempList.append(m)
        for mn in tempList:
            self.add_text(mn[0]) 
        self.add_text("------------------------------------------------------") 
    def characters_player_made(self):
        _msg = self.execute_read_query(self.controller.get_connection(), "SELECT characterName, Level From PlayerCharacter Where AccountName = ‘DoodleMan’;")
        tempList = []
        for m in _msg:
            tempList.append(m)
        for mn in tempList:
            self.add_text(str(mn[0]) + " " + str(mn[1])) 
        self.add_text("------------------------------------------------------")        
        
    def server_protocol(self):
        test = tk.Button(self, text="characters in a given server", command=self.characters_in_given_server)
        self.currentButtons.append(test)
        test.place(relx=0, rely = .1)
        
        _locations = tk.Button(self, text="locations in given server", command=self.locations_in_a_server)
        self.currentButtons.append(_locations)
        _locations.place(relx=0, rely = .3)
    def testCommand(self):
        self.add_text("test")
        self.add_text("------------------------------------------------------") 
    def dwells_in_protocol(self):
        test = tk.Button(self, text="dwells option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=0, rely = .1)
#         print("End server_protocol")
    def player_account_protocol(self):
        test = tk.Button(self, text="p_account option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=0, rely = .1)
        
        characters = tk.Button(self, text="all characters from given player", command=self.characters_player_made)
        self.currentButtons.append(characters)
        characters.place(relx=0, rely = .2)
    def shop_protocol(self):
        test = tk.Button(self, text="shop option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=0, rely = .1)
        
        inventory = tk.Button(self, text="display inventory", command=self.shop_items)
        self.currentButtons.append(inventory)
        inventory.place(relx=0, rely = .2)
                
    def NPC_quest_protocol(self):
        test = tk.Button(self, text="npc quest option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
    def player_character_protocol(self):
        test = tk.Button(self, text="character option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=0, rely = .1)
        
        inventory = tk.Button(self, text="character inventory", command=self.display_characters_items)
        self.currentButtons.append(inventory)
        inventory.place(relx=0, rely = .2)
    def item_protocol(self):
        test = tk.Button(self, text="item option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
    def location_protocol(self):
        test = tk.Button(self, text="location option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
        
        mobs = tk.Button(self, text="get all mobs in location: 1", command=self.mobs_in_location)
        self.currentButtons.append(mobs)
        mobs.place(relx=0, rely = .2)
    def NPC_dialogue_protocol(self):
        test = tk.Button(self, text="npc dialogue option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
        
        dialogue = tk.Button(self, text="display NPC dialogue", command=self.npc_dialogue)
        self.currentButtons.append(dialogue)
        dialogue.place(relx=0, rely = .2)
    def mob_protocol(self):
        test = tk.Button(self, text="mob option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
    def NPC_protocol(self):
        test = tk.Button(self, text="NPC option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=.1, rely = .1)
        
        
        
    def add_text(self, _text):
        self.text.insert(INSERT, "\n\n" + str(_text))
        self.text.yview_moveto('1')
    
    def retreat(self):
        self.controller.show_frame("DatabaseEditFrame")
        
    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")