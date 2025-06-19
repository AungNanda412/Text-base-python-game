class Player: # Player class to create player profile including player's name, player's current position and empty inventory.
    def __init__(self,name,current_position):
        self.location = current_position
        self.name = name
        self.inventory = []

    # Check inventory to display the player's inventory.
    # If inventory is empty, let the player know.
    def check_inv(self):
        if self.inventory == []:
            print(f"You got no items in your inventory")
        else:
            print(f"You open your inventory: {self.inventory}")

    # Prompts the player to input the different direction [North, East, South, West].
    # If player input is invalid, prompts again. If input is valid, return movement.    
    def explore(self):
        flag = True
        while flag == True:
            movement = input("Where you want to move (North, East, South, West):  ").lower()
            if movement != "east" and movement != "west" and movement != "north" and movement != "south":
                print("Invalid command")
                continue
                flag = False
            return movement
        
# Room class to create varioud rooms with different names, description and items.    
class Room:
    def __init__(self,name,description,item):
        self.name = name
        self.description = description
        self.item = item

    # Set the connection between rooms with direction [North, East, South, West]
    # Each direction is connected to another room. None value mean there is no connected direction.
    def set_connection(self,north = None,east = None,south = None,west = None):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
    # Method for player to check item depend on current location
    # If items are in the room, it displayed to player
    #If items are not in the room, notify the player that item is not in this room.
    def check_item(self):
        if self.item:
            print(f"You found these items in this dimension:{self.item}")
        else:
            print("There is nothing useful here")
    
    

# Chest class to create various chest with different names, descriptions and items
class Chest:
    def __init__(self,chest_name,description,items =[]):
        self.chest_name = chest_name
        self.description = description
        self.item = items
        
# Main game class to create various method               
class Game:
    def __init__(self):
        self.chest =[Chest("Soul Keeper Grave","Grave that seal the souls",["Pure soul","Pure soul","Pure soul","Pure soul"]),
                     Chest("Golden Chest","For the Dungeon Master!",["Soul Keeper Lantern"]),
                     Chest("Treasure Of Ocean","Ruin it!!",["Death Soul"]),
                     Chest("Empty Chest","Nothing inside",[]),
                     Chest("Empty_Chest","Nothing inside,beware of Mimic!",[]),
                     Chest("Empty_Chest2","It's the Mimic! Run!",[])]
        self.room =[
            Room("Entrance","The Entrance of The Dungeon",None),
            Room("Grave of the Soul Keeper","All the souls are gatherd here",self.chest[0]),
            Room("Junction-1","The Junction in the middle of hallway",self.chest[3]),
            Room("Room-2","Random Dimension",self.chest[1]),
            Room("Junction-2","The Junction in the middle of hallway",self.chest[4]),
            Room("The Void","The Domain of Emptiness(you can store items here)",[]),
            Room("Wrath Domain","You have enterd the wrong place! Mortal! DIE! God of Wrath damage your soul",["Blood"]),
            Room("Junction-3","The Junction in the middle of hallway",self.chest[5]),
            Room("Treasure Domain","With this treasure...summon our master back",["iron","iron","iron","iron"]),
            Room("Ocean Domain","The Domain filling with magical liquid",self.chest[2]),
            Room("Junction-4","The Junction in the middle of hallway",None),
            Room("Treasure Holder","Don't bother me you mortal,What do you want?!!",["Nature Soul","Magma Heart","Dungeon Core","Core","Spirit"]),
            Room("Jungle Dimension","The only peaceful place of the dungeon",["Herb","Herb","Herb","Herb","Herb"]),
            Room("Divine General's Dimension","The room full of menacing aura",["Divine General's Soul"]),
            Room("Dungeon Master","This is where your villian arc start! Revive the Dungeon Master!",[])
        ]
        self.player = Player(input("Enter your name: "),self.room[0])
    # Create the game map using set_connection method  
    def creat_map(self):
        self.room[0].set_connection(north=None,east=self.room[2],south=None,west=None)
        self.room[1].set_connection(north=self.room[2],east=None,south=None,west=None)
        self.room[2].set_connection(north=self.room[3],east=self.room[4],south=self.room[1],west=self.room[0])
        self.room[3].set_connection(north=None,east=None,south=self.room[2],west=None)
        self.room[4].set_connection(north=self.room[5],east=self.room[7],south=self.room[6],west=self.room[2])
        self.room[5].set_connection(north=None,east=None,south=self.room[4],west=None)
        self.room[6].set_connection(north=self.room[4],east=None,south=None,west=None)
        self.room[7].set_connection(north=self.room[8],east=self.room[10],south=self.room[9],west=self.room[4])
        self.room[8].set_connection(north=None,east=None,south=self.room[7],west=None)
        self.room[9].set_connection(north=self.room[7],east=None,south=None,west=None)
        self.room[10].set_connection(north=self.room[11],east=self.room[13],south=self.room[12],west=self.room[7])
        self.room[11].set_connection(north=None,east=None,south=self.room[10],west=None)
        self.room[12].set_connection(north=self.room[10],east=None,south=None,west=None)
        self.room[13].set_connection(north=None,east=self.room[14],south=None,west=self.room[10])
        self.room[14].set_connection(north=None,east=None,south=None,west=self.room[13])

    # Locate the player's current locaton.
    # Check player's current location and print the infomation of current room.
    def locate(self):
        if self.player.location == self.room[0]:
            print(f"You are at the {self.room[0].name}")
            print(f"{self.room[0].description}")
            print(f"Chest: {self.room[0].item}")
        elif self.player.location == self.room[1]:
            print(f"You are at the {self.room[1].name}")
            print(f"{self.room[1].description}")
            print(f"Chest: {self.room[1].item.chest_name}")
            print(f"{self.room[1].item.description}")
        elif self.player.location == self.room[2]:
            print(f"You are at the {self.room[2].name}")
            print(f"{self.room[2].description}")
            print(f"Chest: {self.room[2].item.chest_name}")
            print(f"{self.room[2].item.description}")
        elif self.player.location == self.room[3]:
            print(f"You are at the {self.room[3].name}")
            print(f"{self.room[3].description}")
            print(f"Chest: {self.room[3].item.chest_name}")
            print(f"{self.room[3].item.description}")
        elif self.player.location == self.room[4]:
            print(f"You are at the {self.room[4].name}")
            print(f"{self.room[4].description}")
            print(f"Chest: {self.room[4].item.chest_name}")
            print(f"{self.room[4].item.description}")
        elif self.player.location == self.room[5]:
            print(f"You are at the {self.room[5].name}")
            print(f"{self.room[5].description}")
            print(f"Chest: None")
            
        elif self.player.location == self.room[6]:
            print(f"You are at the {self.room[6].name}")
            print(f"{self.room[6].description}")
            print(f"Chest: None")
            
        elif self.player.location == self.room[7]:
            print(f"You are at the {self.room[7].name}")
            print(f"{self.room[7].description}")
            print(f"Chest: {self.room[7].item.chest_name}")
            print(f"{self.room[7].item.description}")
        elif self.player.location == self.room[8]:
            print(f"You are at the {self.room[8].name}")
            print(f"{self.room[8].description}")
            print(f"Chest: None")
            
        elif self.player.location == self.room[9]:
            print(f"You are at the {self.room[9].name}")
            print(f"{self.room[9].description}")
            print(f"Chest: {self.room[9].item.chest_name}")
            print(f"{self.room[9].item.description}")
        elif self.player.location == self.room[10]:
            print(f"You are at the {self.room[10].name}")
            print(f"{self.room[10].description}")
            print(f"Chest: {self.room[10].item}")
            
        elif self.player.location == self.room[11]:
            print(f"You are at the {self.room[11].name}")
            print(f"{self.room[11].description}")
            print(f"Chest: None")
            
        elif self.player.location == self.room[12]:
            print(f"You are at the {self.room[12].name}")
            print(f"{self.room[12].description}")
            print(f"Chest: None")
            
        elif self.player.location == self.room[13]:
            print(f"You are at the {self.room[13].name}")
            print(f"{self.room[13].description}")
            print(f"Chest: None")
            
        elif self.player.location == self.room[14]:
            print(f"You are at the {self.room[14].name}")
            print(f"{self.room[14].description}")
            print(f"Chest: None")
            
    # Locate the items list base on player's location.
    # Check player's current location and print the items from that location.
    # If no item present in current location of player, let the player know.
    def locate_item(self):
        if self.player.location == self.room[5]:
            self.player.location.check_item()
            
        elif self.player.location == self.room[6]:
            self.player.location.check_item()
        elif self.player.location == self.room[8]:
            self.player.location.check_item()
        elif self.player.location == self.room[11]:
            self.player.location.check_item()
        elif self.player.location == self.room[12]:
            self.player.location.check_item()
        elif self.player.location == self.room[13]:
            self.player.location.check_item()
        elif self.player.location == self.room[14]:
            self.player.location.check_item()
        else:
            if self.player.location == self.room[0]:
                print("You see no items in this dimension")
            else:
                print("You see no items in this dimension, but something shiny!")
    # Allow the player to move 4 different direction (North, East, South, West)
    # If the player move toward direction which is not connected with any room, notify player that it is impossible to go there.

    def move_player(self, direction):
        if direction == "east" and self.player.location.east:
            self.player.location = self.player.location.east
            print(f"You travel to {self.player.location.name}")
        elif direction == "west" and self.player.location.west:
            self.player.location = self.player.location.west
            print(f"You travel to {self.player.location.name}")
        elif direction == "north" and self.player.location.north:
            self.player.location = self.player.location.north
            print(f"You travel to {self.player.location.name}")
        elif direction == "south" and self.player.location.south:
            self.player.location = self.player.location.south
            print(f"You travel to {self.player.location.name}")
        else:
            print("You can't travel through the wall")

    # Allow the player to take items from the chest in the room.
    # Player inventory can store only 4 items, if the player taking item with full inventory, let the player know it can't
    # If chest exist in player location, player can take item from chest. If not, let the player know no chest is there.
    # Correct item names are required to take item from chest, if player type the name wrong, let the player know the item is not there.
    def take_item_from_chest(self):
        item = input("Type the name of item you want to take : ")
        if len(self.player.inventory) < 4:
            
            if  self.player.location.item == self.chest[0]:
                if item in self.chest[0].item:
                    self.player.inventory.append(item)
                    self.chest[0].item.remove(item)
                    print(f"You took {item} from the chest")
                else:
                    print(f"{item} is not in the chest.")
                    return None
            elif  self.player.location.item == self.chest[1]:        
                if item in self.chest[1].item:
                    self.player.inventory.append(item)
                    self.chest[1].item.remove(item)
                    print(f"You took {item} from the chest")
                else:
                    print(f"{item} is not in the chest.")
                    return None
            elif  self.player.location.item == self.chest[2]:
                if item in self.chest[2].item:
                    self.player.inventory.append(item)
                    self.chest[2].item.remove(item)
                    print(f"You took {item} from the chest")
                else:
                    print(f"{item} is not in the chest.")
                    return None
            elif  self.player.location.item == self.chest[3]:
                if item in self.chest[3].item:
                    self.player.inventory.append(item)
                    self.chest[3].item.remove(item)
                    print(f"You took {item} from the chest")
                else:
                    print(f"{item} is not in the chest.")
                    return None
            elif  self.player.location.item == self.chest[4]:
                if item in self.chest[4].item:
                    self.player.inventory.append(item)
                    self.chest[4].item.remove(item)
                    print(f"You took {item} from the chest")
                else:
                    print(f"{item} is not in the chest.")
                    return None
            elif  self.player.location.item == self.chest[5]:
                if item in self.chest[5].item:
                    self.player.inventory.append(item)
                    self.chest[5].item.remove(item)
                    print(f"You took {item} from the chest")
                else:
                    print(f"{item} is not in the chest.")
                    return None
            else:
                print("The chest is not in this dimension")
        else:
            print("Your can't take item, your inventory is full. Find empty chest to store items")

    # Allow the player to pick up item from the room.
    # Player inventory can store only 4 items, if the player picking up item with full inventory, let the player know it can't.
    # If item exist in player location, player can pick up item from the room. If not, let the player know no item is there.
    # Correct item names are required to pick up item from the room, if player type the name wrong, let the player know the item is not there.   
    def take_item_from_room(self):
        item = input("Type the name of the item you want to pick up : ")
        if len(self.player.inventory) < 4:
            if self.player.location == self.room[5]:
                if item in self.room[5].item:
                    self.player.inventory.append(item)
                    self.room[5].item.remove(item)
                    print(self.room[5].item)
                else:
                    print(f"There is no {item} in this dimension")
                    return None
                    
            elif self.player.location == self.room[6]:    
                if item in self.room[6].item:
                    self.player.inventory.append(item)
                    self.room[6].item.remove(item)
                    print(self.room[6].item)
                else:
                    print(f"There is no {item} in this dimension")
                    return None

            elif self.player.location == self.room[8]:    
                if item in self.room[8].item:
                    self.player.inventory.append(item)
                    self.room[8].item.remove(item)
                    print(self.room[8].item)
                else:
                    print(f"There is no {item} in this dimension")
                    return None

            elif self.player.location == self.room[12]:    
                if item in self.room[12].item:
                    self.player.inventory.append(item)
                    self.room[12].item.remove(item)
                    print(self.room[12].item)
                else:
                    print(f"There is no {item} in this dimension")
                    return None

            elif self.player.location == self.room[13]:
                if item in self.room[13].item:
                    self.player.inventory.append(item)
                    self.room[13].item.remove(item)
                    print(self.room[13].item)
                else:
                    print(f"There is no {item} in this dimension")
                    return None
            elif self.player.location == self.room[14]:
                if item in self.room[14].item:
                    self.player.inventory.append(item)
                    self.room[14].item.remove(item)
                    print(self.room[14].item)
                else:
                    print(f"There is no {item} in this dimension")
                    return None
            else:
                print("You can't pick up item from this room")
        else:
            print("You can't take item, your inventory is full. Find the void to store items")

    # Allow the player to place item in the room.
    # Player have to type the correct item name they have inside their inventory if they want to store item in the room. 
    # If not, let the player know the item they want to store is not in their inventory.
    def place_item(self):
        
            
        item = input("Type the item name you want to place inside: ")
        if item in self.player.inventory:
            self.player.location.item.append(item)
            self.player.inventory.remove(item)
            
        else:
            print(f"You don't have {item} in your inventory")
            
    # Allow the player to trade items base on different recipes.
    # If item_1 and item_2 are placed in order, player will obtain new item and trade success.
    # If not, let the player know trade was fail.       
    def trading(self):
        item_1 = input("Choose item to place on crafting table: ")
        item_2 = input("Choose item to place on crafting table: ")
        
        if item_1 in self.player.inventory and item_2 in self.player.inventory:
            self.room[11].item.append(item_1)
            self.room[11].item.append(item_2)
            self.player.inventory.remove(item_1)
            self.player.inventory.remove(item_2)
            if item_1 == "Herb" in self.room[11].item and item_2 == "Pure soul" in self.room[11].item:
                
                self.player.inventory.append("Nature Soul")
                self.player.location.item.remove("Nature Soul")
                print("Trade Successful")
            elif item_1 == "Blood" in self.room[11].item and item_2 == "Soul Keeper Lantern" in self.room[11].item:

                self.player.inventory.append("Magma Heart")
                self.player.location.item.remove("Magma Heart")
                print("Trade Successful")
            elif item_1 == "Divine General's Soul" in self.room[11].item and item_2 == "iron" in self.room[11].item:

                self.player.inventory.append("Spirit")
                self.player.location.item.remove("Spirit")
                print("Trade Successful")
            elif item_1 == "Nature Soul" in self.room[11].item and item_2 == "Death Soul" in self.room[11].item:

                self.player.inventory.append("Core")
                self.player.location.item.remove("Core")
                print("Trade Successful")
            elif item_1 == "Core" in self.room[11].item and item_2 == "Spirit" in self.room[11].item:

                self.player.inventory.append("Dungeon Core")
                self.player.location.item.remove("Dungeon Core") 
                print("Trade Successful")  
        else:
            print("Trade was unsuccessful")

    # Allow the player to open chest and see which item inside
    # Print the chest info and items of player current location.
    def open_chest(self):
        print(f"You found {self.player.location.item.chest_name}")
        print(f"Inside the {self.player.location.item.chest_name} : {self.player.location.item.item}")

    # Main game loop to manage player action.
    # Calling back all the require method above here in the loop.
    def press_start(self):
        while True:
            if self.player.name == "":
                self.player.name = input("Enter your name: ")
            else:
                break
        
        game_status = False 
        print(f"You are at the Entrance of the old dungeon [{self.player.name}], your quest is to revive the dungeon master")
        print("Villian arc begin!!")
        
        while True:
            
            print()
            if not game_status:
                action = input("Choose action: [Inventory], [Move], [Locate], [Trade], [Pick], [Open Chest], [Revive], [Chest], [Store]: ").lower()
                if action == "move":
                    direction = self.player.explore()
                    self.move_player(direction)
                elif action == "locate":
                    
                    self.locate()
                    self.locate_item()
                    print("**If you want to pick up item use [pick]**")
                    print("**If you see chest,you can check it first with [chest] and then use [open chest] to take item**")
                elif action == "chest":
                    if type(self.player.location.item) == type(list()):
                        print("There is no chest in this dimension.")
                    else:    
                        if self.player.location.item == None:
                                print("There is no chest in this dimension.")
                        else:
                            self.open_chest()
                    
                elif action == "inventory":
                    self.player.check_inv()
                elif action == "pick":
                    if not self.player.location.item in self.chest and self.player.location.item != None:
                        print("Reminder!- Make sure to input the item name correctly.(items from chest and room)")
                        ask = input("You want to pick up item? YES/NO: ").lower()
                        
                        if ask == "yes":
                            self.take_item_from_room()
                        else:
                            if ask == "no":
                                pass
                            else:
                                print("Invalid Command")
                    else:
                        print("There is no item to pick up")
                elif action == "open chest":
                    if self.player.location.item in self.chest:
                        print("Reminder!- Make sure to input the item name correctly.(items from chest and room)")
                        ask = input("You want to take item from chest? YES/NO: ").lower()
                        
                        if ask == "yes":
                            self.take_item_from_chest()
                        else:
                            if ask == "no":
                                pass
                            else:
                                print("Invalid Command")
                        
                    else:
                        print("There is no chest in this dimension.")
                        
                elif action == "trade":
                    if self.player.location == self.room[11]:
                        print("Recipe: Herb(item1(first)) and Pure soul(item2(second)) for [Nature Soul]")
                        print()
                        print("Recipe: Blood(item1(first)) and Soul Keeper Lantern(item2(second)) for [Magma Heart]")
                        print()
                        print("Recipe: Divine General's Soul(item1(first)) and iron(item2(second)) for [Spirit]")
                        print()
                        print("Recipe: Nature Soul(item1(first)) and Death Soul(item2(second)) for [Core]")
                        print()
                        print("Recipe: Core(item1(first)) and Spirit(item2(second)) for [Dungeon Core]")
                        print()
                        print("[[Place the items in order as shown in recipes.]]")
                        self.trading()
                    else:
                        print("You need to find the [Treasure Holder] first.")
                elif action == "revive":
                    if self.player.location == self.room[14]:
                        print("You need to place [Magma Heart] and [Dungeon Core] to revive the Dungeon Master")
                        self.place_item()
                        if "Dungeon Core" in self.room[14].item and "Magma Heart" in self.room[14].item:
                            game_status = True
                        else:
                            print(f"Inside Dungeon Master Core: {self.room[14].item}")
                            print("Require more Souls")
                    else:
                        print("You are not in the [{Dungeon Master's Domain}].")
                elif action == "store":
                    if self.player.location == self.room[5]:
                        self.place_item()
                    else:
                        print("You are not in the [void].")
                else:
                    print("Invalid Command.")

            else:
                print(f"{self.player.name.upper()},YOU HAVE AWAKENED THE DUNGEON MASTER!!")        
                print("WITH THIS TREASURE...I SUMMON THE LEGENDARY DUNGEON MASTER!!!")
                print("You unlock new path: Villian arc...")
                print("You have completed the game.")

                break
            

            print()
            
            
            
        
game = Game()
game.creat_map()
game.press_start()
    
        
    
            


        