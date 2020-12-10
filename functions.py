import mysql.connector
import tkinter as tk
import PIL
from mysql.connector import Error
from tkinter import *
from PIL import ImageTk, Image
from asyncio.base_events import Server
import tkinter.simpledialog as simpledialog
from tkinter import messagebox

class functionFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#323232")
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
        
    #below are the many functions the server can perform from the functions Frame
    def helper(self, query):
            _msg = self.execute_read_query(self.controller.get_connection(), query)
            tempList = []
            for m in _msg:
                tempList.append(m)
            if tempList.__len__() == 0:
                raise ValueError
            return tempList
        
    def characters_in_given_server(self):
        try:
            input = simpledialog.askstring("Server Input", "type a server ID")
            if input==None:
                return
            query = "SELECT charactername, ServerID FROM playercharacter WHERE ServerID = " + input + ";"
            test_list = self.helper(query)             
            self.add_text("_____Characters in Server: " + str(input))
            for mn in test_list:
                self.add_text(" -Character: " + str(mn[0]) + " --- Server: " + str(mn[1]))
            self.add_text("------------------------------------------------------") 
        except ValueError:
            messagebox.showerror("404", "no data matches your query..")
            self.characters_in_given_server()
        except:
            messagebox.showerror("Error", "Invalid Server ID")
            self.characters_in_given_server()
            
    def characters_at_location(self):
        try:
            input = simpledialog.askstring("Location Input", "type a location ID")
            if input==None:
                return
            query = "SELECT charactername From PlayerCharacter Where locationID=" + input + ";"
            self.add_text("_____Characters in Location: " + str(input))
            for mn in self.helper(query):
                self.add_text(str(" -Character: " + mn[0]))
            self.add_text("------------------------------------------------------") 
        except ValueError:
            messagebox.showerror("404", "no data matches your query..")
            self.characters_at_location()
        except:
            messagebox.showerror("Error", "Invalid location ID")
            self.characters_at_location()
            
    def mobs_in_location(self):
        try:
            input = simpledialog.askstring("Location Input", "type a location ID")
            if input==None:
                return
            query = "select mobid,type From mob Where locationID=" + input + " ORDER BY type;"
            self.add_text("_____Mobs in Location: " + str(input))
            for mn in self.helper(query):
                self.add_text(" -Mob ID: " + str(mn[0]) + " --- Mob Type: " + str(mn[1]))
            self.add_text("------------------------------------------------------") 
        except ValueError:
            messagebox.showerror("404", "no data matches your query..")
            self.mobs_in_location()
        except Error as e:
            messagebox.showerror("Error", "Invalid location ID")
            self.mobs_in_location()
        
    def npc_dialogue(self):
        try:
            input = simpledialog.askstring("NPC Input", "type an NPC ID")
            if input==None:
                return
            query = "Select dialogue From Npcdialogue Where npcid =" + input + ";"
            self.add_text("_____Dialogue from NPC: " + str(input))
            for mn in self.helper(query):
                self.add_text(" -Dialogue Option: " + str(mn))
            self.add_text("------------------------------------------------------") 
        except ValueError:
            messagebox.showerror("404", "no data matches your query..")
            self.npc_dialogue()
        except Error as e:
            messagebox.showerror("Error", "Invalid NPCID")
            self.npc_dialogue()
            
    def locations_in_a_server(self):
        try:
            input = simpledialog.askstring("Server Input", "type a Server ID")
            if input==None:
                return
            query = "Select locationid, LocationName From location Where serverid = " + input + ";"
            self.add_text("_____Locations in Server: " + str(input))
            for mn in self.helper(query):
                self.add_text(" -Location: " + str(mn[1]) + " --- ID: " + str(mn[0]))
            self.add_text("------------------------------------------------------") 
        except ValueError:
            messagebox.showerror("404", "no data matches your query..")
            self.locations_in_a_server()
        except Error as e:
            messagebox.showerror("Error", "Invalid server ID")
            self.locations_in_a_server()
            
    def display_characters_items(self):
        
        try:
            input = simpledialog.askstring("Character Input", "type a Character Name")
            if input==None:
                return
            query = "select ItemName from item where CharacterName = '" + input + "';"
            self.add_text("_____Items in Inventory: " + str(input))
            for mn in self.helper(query):
                self.add_text(" -Item: " + str(mn))
            self.add_text("------------------------------------------------------")
        except ValueError:
            messagebox.showerror("404", "no data matches your query..")
            self.display_characters_items() 
        except Error as e:
            messagebox.showerror("Error", "Invalid Character Name")
            self.display_characters_items()
            
    def characters_player_made(self):
        try:
            input = simpledialog.askstring("Account Input", "type an account name")
            if input==None:
                return
            query = "select characterName,Level FROM PlayerCharacter WHERE AccountName='" + input + "';"
            self.add_text("_____characters " + str(input) + " has made: ")
            for mn in self.helper(query):
                self.add_text(str(" -Name: " + mn[0]) + " --- Level: " + str(mn[1]))
            self.add_text("------------------------------------------------------")
        except ValueError:
            messagebox.showerror("404", "no data matches your query..")
            self.characters_player_made() 
        except Error as e:
            messagebox.showerror("Error", "Invalid Character Name")
            self.characters_player_made()
            
    def servers_location_in(self):   
        _msg = self.execute_read_query(self.controller.get_connection(), "Select serverid,LocationName From location;")
        tempList = []
        self.add_text("_____list Servers/locations")
        for m in _msg:
            tempList.append(m)
        for mn in tempList:
            self.add_text(str(" -Server: " + str(mn[0])) + " Location: " + str(mn[1])) 
        self.add_text("------------------------------------------------------") 
    
    def testCommand(self):
        self.add_text("test")
        self.add_text("------------------------------------------------------") 
        
    def mob_count_location(self):
        try:
            input = simpledialog.askstring("Location Input", "type a location ID")
            if input==None:
                return
            query = "Select count(*) from mob Where locationID =" + input + ";"
            self.add_text("_____Total Mobs in location:  " + str(input))
            for mn in self.helper(query):
                self.add_text(" -Count: " + str(mn[0]))
            self.add_text("------------------------------------------------------")
        except ValueError:
            messagebox.showerror("404", "no data matches your query..")
            self.mob_count_location() 
        except Error as e:
            messagebox.showerror("Error", "Invalid LocationID")
            self.mob_count_location()
            
    def display_all_accounts(self):
        try:
            query = "Select accountname, email, password From playeraccount;"
            self.add_text("_____All Player Accounts:  ")
            for mn in self.helper(query):
                self.add_text(" -Account: " + str(mn[0]) + "\n email:  " + str(mn[1]) + "\n password:  " + str(mn[2]))
            self.add_text("------------------------------------------------------")
        except ValueError:
            messagebox.showerror("404", "no data matches your query..")
            self.display_all_accounts() 
        except Error as e:
            messagebox.showerror("Error", "Invalid LocationID")
            self.display_all_accounts()
            
    def display_items_in_shop(self):
        try:
            input = simpledialog.askstring("Shop Input", "type a Shop ID")
            if input==None:
                return
            query = "Select itemid, itemName From item Where shopID=" + input + ";"
            self.add_text("_____All Items in Shop: " + str(input))
            for mn in self.helper(query):
                self.add_text(" -Item ID: " + str(mn[0]) + "\n Name:  " + str(mn[1]))
            self.add_text("------------------------------------------------------")
        except ValueError:
            messagebox.showerror("404", "no data matches your query..")
            self.display_items_in_shop() 
        except Error as e:
            messagebox.showerror("Error", "Invalid LocationID")
            self.display_items_in_shop()
        
    #below are the protocols for placing and setting the buttons and their behavior on
    #the left pane of the function screen. One protocol is called depending on the 
    #what the current Table is.
    
    #2 complete buttons -----UF
    def server_protocol(self):
        
        test2 = tk.Button(self, text="characters in a given server", command=self.characters_in_given_server)
        self.currentButtons.append(test2)
        test2.place(relx=0, rely = .2)
        
        _locations = tk.Button(self, text="locations in given server", command=self.locations_in_a_server)
        self.currentButtons.append(_locations)
        _locations.place(relx=0, rely = .3)
        
    #0 complete buttons -----UF
    def dwells_in_protocol(self):
        print("no protocols for DwellsIn")
    
    #2 complete button -----UF
    def player_account_protocol(self):
        test = tk.Button(self, text="Display All Accounts", command=self.display_all_accounts)
        self.currentButtons.append(test)
        test.place(relx=0, rely = .1)
        
        characters = tk.Button(self, text="all characters from given player", command=self.characters_player_made)
        self.currentButtons.append(characters)
        characters.place(relx=0, rely = .2)
        
        test3 = tk.Button(self, text="place Holder", command=self.testCommand)
        self.currentButtons.append(test3)
        test3.place(relx=0, rely = .3)
        
    #1 complete buttons -----UF
    def shop_protocol(self):
        
        inventory = tk.Button(self, text="display inventory", command=self.display_items_in_shop)
        self.currentButtons.append(inventory)
        inventory.place(relx=0, rely = .2)
 
    #0 complete buttons -----UF
    def NPC_quest_protocol(self):
        print("no npc quest protocols")
        
    #1 complete button -----UF
    def player_character_protocol(self):
        inventory = tk.Button(self, text="character inventory", command=self.display_characters_items)
        self.currentButtons.append(inventory)
        inventory.place(relx=0, rely = .3)
        
    #0 complete buttons -----UF
    def item_protocol(self):
        print("no item protocols")
        
    #3 complete buttons -----GOOD
    def location_protocol(self):
        mobs = tk.Button(self, text="all mobs in location", command=self.mobs_in_location)
        self.currentButtons.append(mobs)
        mobs.place(relx=0, rely = .1)
        
        servs = tk.Button(self, text="all servers a location is in", command=self.servers_location_in)
        self.currentButtons.append(servs)
        servs.place(relx=0, rely = .2)
        
        chars = tk.Button(self, text="Characters at location", command=self.characters_at_location)
        self.currentButtons.append(chars)
        chars.place(relx=0, rely = .3)
    
    #2 complete button -----UF
    def NPC_dialogue_protocol(self):
        test = tk.Button(self, text="npc dialogue option", command=self.testCommand)
        self.currentButtons.append(test)
        test.place(relx=0, rely = .1)
        
        dialogue = tk.Button(self, text="display NPC dialogue", command=self.npc_dialogue)
        self.currentButtons.append(dialogue)
        dialogue.place(relx=0, rely = .2)
        
        
    #1 complete buttons -----UF
    def mob_protocol(self):
        test = tk.Button(self, text="Total Mobs", command=self.mob_count_location)
        self.currentButtons.append(test)
        test.place(relx=0, rely = .1)
        
        
    #0 complete buttons -----UF
    def NPC_protocol(self):
        print("no NPC protocols")
        
    #END LEFT PANE BUTTON PROTOCOLS--------------------------------------------
        
        
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