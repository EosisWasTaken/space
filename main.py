# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 08:42:45 2022
@author: CERDANA
"""

import random
import sys
import time
import os

os.system('color')


SECTOR_SIZE = 9
SUBSECTOR_SIZE = 9

game = True



clear = lambda: os.system('cls')


def typewrite(text,speed=0.030):
    for char in text:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()

def choice(text,*choices):
    typewrite(text)
    ch = {}
    decided = False
    for choice in choices:
        ch[choices.index(choice)+1] = choice
    while not decided:
        e = input(">>> ")
        print(e,ch.keys())
        try:
            if int(e) in ch.keys():
                typewrite(ch[int(e)])
                decided = True
                return int(e)
            else:
                print("You can't do this.")
        except ValueError:
            print("You can't do this.")

def colorstring(text,c):
    match c:
        case "PURPLE":
            return str(colors.PURPLE + text + colors.END)
        case "BLUE":
            return str(colors.BLUE + text + colors.END)
        case "CYAN":
            return str(colors.CYAN + text + colors.END)
        case "GREEN":
            return str(colors.GREEN + text + colors.END)
        case "YELLOW":
            return str(colors.YELLOW + text + colors.END)
        case "FAIL":
            return str(colors.FAIL + text + colors.END)
        case "BOLD":
            return str(colors.BOLD + text + colors.END)
        case "UNDERLINE":
            return str(colors.UNDERLINE + text + colors.END)

class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Inventory:
    def __init__(self,name,maxInvSize):
        self.inv = {}
        self.maxInvSize = maxInvSize
        self.name = name

    def update_maxInvSize(self,amount):
        if amount > 0:
            self.maxInvSize += amount
            return self.maxInvSize
        elif amount < 0:
            self.maxInvSize -= amount
            return self.maxInvSize
        else:
            return False

    def get_weight(self):
        weight = 0
        for i in self.inv.values():
            weight += i
        return weight

    def is_full(self):
        return self.get_weight() > self.maxInvSize

    def add_item(self,item,quantity):
        if not self.is_full():
            if self.get_weight() + quantity < self.maxInvSize:
                if item.title() in self.inv:
                    self.inv[item.title()] += quantity
                else:
                    self.inv[item.title()] = quantity

    def remove_item(self,item,quantity):
        if item.title() in self.inv:
            if quantity >= self.inv[item.title()]:
                del self.inv[item.title()]
            else:
                self.inv[item.title()] -= quantity

    def get_inv(self):
        return self.inv

    def print_inv(self):
        print(str(self.name) + " : ")
        for i in self.inv:
            print("| " + str(i) + " (" + str(self.inv[i]) + ")")
        print("Space used : " + str(self.get_weight()) + " / " + str(self.maxInvSize))

    def has_item(self,item):
        if item.title() in self.inv:
            return self.inv[item.title()]
        else:
            return -1


class Player:
    def __init__(self,name="None",spaceship="None") -> None:
        self.name = name
        self.hp = 60
        self.inv = Inventory("Backpack",40)
        self.spaceship = spaceship
        self.pos = "Your spaceship"




class PilotableSpaceship:
    def __init__(self,name="None",pilot="None"):
        self.inv = Inventory("Cargo",300)
        self.fuel = 100
        self.name = name
        self.pilot = pilot
        self.slots = {
            "1" : None,
            "2" : None,
            "3" : None,
            "4" : None,
            "5" : None
        }
        self.pos = [0,0,0,0]


    def install_on_slot(self,slot,tech):
        pass

    def uninstall_on_slot(self,slot,tech):
        pass

class World:
    def __init__(self):
        self.world = []

    def build_world(self):
        for x in range(SECTOR_SIZE+1): # Sector X axis
            self.world.append([])
            for y in range(SECTOR_SIZE+1): # Sector Y axis
                #self.world[x].append("Sector " + str(x) + " / " + str(y))
                self.world[x].append([])
                for a in range(SUBSECTOR_SIZE+1): # Subsector X axis
                    self.world[x][y].append([])
                    for b in range(SUBSECTOR_SIZE+1): # Subsector Y axis
                        self.world[x][y][a].append("Sector " + str(x) + " : " + str(y) + " / Subsector " + str(a) + " : " + str(b))


class Planet:
    def __init__(self) -> None:
        self.hasAtmosphere = True
        self.gravity = 0
        self.weather = None
        self.size = 0
        self.map = []

    def build_planet(self):
        self.size = random.randint(3,10)
        for x in range(self.size):
            self.map.append([])
            for y in range(self.size):
                self.map[x].append([])
                self.map[x][y].append(str(x) + str(y))


class GroundBase:
    def __init__(self):
        self.name = ""
        self.inv = Inventory(self.name,random.randint(10,150))

class Spaceship:
    pass

class Station:
    pass

class LootGenerator:
	def __init__(self):
		pass

	def generate_loot(self,amount,raritycap):
		pass


class Game:
    def __init__(self):
        self.MOVE = ["move","go","thrust","to","dir","direction"]
        self.player = None

    def print_hud(self):
        self.center_print(colorstring("< S p a c e  G a m e >","PURPLE"))
        print(self.lr_justify("Position : ","You are at : "))
        spsec = ("Sector " + str(X.player.spaceship.pos[0]) + ":" + str(X.player.spaceship.pos[1]))
        spsub = ("Sub-sector " + str(X.player.spaceship.pos[2]) + ":" + str(X.player.spaceship.pos[3]))
        print(self.lr_justify(spsec,str(X.player.pos)))
        print(self.lr_justify(spsub,"????"))

    def start_game(self):
        print("< S p a c e  g a m e >")
        P = Player()
        S = PilotableSpaceship()
        P.name,S.name = faststart()
        S.pilot = P
        P.spaceship = S
        self.player = P
        P.pos = S.name
        print("ok")
        self.main_loop()

        
    def main_loop(self):
        while game:
            clear()
            self.print_hud()
            inp = self.user_input("Action")
            self.parse_input(inp)

    def print_info(self,title,message):
        return str(title).capitalize() + " >> " + str(message)

    def user_input(self,message):
        return input(str(message) + " >>> ").lower()

    def center_print(self,text):
        width = os.get_terminal_size().columns
        print(text.center(width))

    def lr_justify(self,left, right):
        return '{}{}{}'.format(left, ' ' * (os.get_terminal_size().columns - len(right + left)), right)

    def parse_input(self,inp):
        cmd = inp.split()



W = World()
W.build_world()
print(W.world)
print(W.world[5][7][9][3])

def start():
    typewrite("You wake up, feeling half-asleep. \n")
    typewrite("As you open your eyes, you notice a blue-ish glass right in front of your eyes. \n")
    typewrite("What do you decide to do ? ")
    choice("You could look around(1), or try to call for help(2) \n","You look around you. Your whole body is laying on something that feels like moss, and upon looking at your feet, you notice you are trapped in a box.","You call for help, but as you shout, you notice your voice is really loud. No one heard you, because you are trapped in what seems to be a box.")
    typewrite("As your mind starts to race to find answers to all your questions, a red light starts to ??? and your coffin opens. The temperature difference between the bow you were in and the exterior is so high that fog starts to form. \n")
    typewrite("You get out of the box, and look around you. You are in a dark room, slightly ??? by a halo of light coming from the box you woke up from. \n")
    typewrite("Suddenly, a bright voice comes from a corner of the room : \n")
    colorprint("MAJOR ISSUE DETECTED ... INITIATED W.A.K.E SEQUENCE FOR ALL APPLICABLE MEMBERS ... TOTAL : ONE ... ","BOLD")
    typewrite("Your head suddenly hurts. A lot. A moment later, the voice stops, and so does your headache. \n")
    typewrite("Now, you feel like you know everything. You still have tons of questions, and, standing in the middle of this room, you start to search answers. You think, and you remember that your are (enter your name) \n")
    name = str(input(""))
    typewrite(", and you are 25. You remember getting into the box. They are made to make you sleep over very long times. You can also remember where you are, in the same room as all the crewmates of your expedition. You were all astronauts, but you cannot remember what is the point of your presence here, what was the mission, or your expdition. All you can remember is the name of the ship, Valkyria. You have too much questions going thourgh your head, but the voice starts to talk once again. \n")
    colorprint("MAJOR ISSUE DETECTED ... IMPACT IN FIVE MINUTES ... ALL MEMBRS HAVE TO EVACUATE THIS SHIP ... NECESSARY ARE BEING SENT TO GROUND CONTROL ... ... CANNOT REACH GROUND CONTROL ... PROCEDURE CANCELLED ... PLEASE EVACUATE THIS SHIP","BOLD")
    typewrite("Suddenly, a thin red light appears on the ground. Upon looking at it, it looks like a path. Stressed and kind of disoriented, you decide to follow it. \n")
    typewrite("You pass trhough the door, multiple corridors, another dorm room, and even something that looks like e bar. As you run thourgh these rooms, you remember bits of memories that happened in these places. Life must have been cool here, but now everything is finished, and you are th only one not asleep here \n")
    typewrite("Then, you arrive at the Hangar 101. The red path stops there, and as you look up, you see a medium-sized ship with it's cargo door opened. \n")
    typewrite("""Right under the cockpit's glass, you see the inscription (enter the name of the ship here)" """)
    shipname = str(input(""))
    typewrite(""" ", a very awesome name for this ship. You decide to get into the ship. As you are walking, you can hear the voice starting the same ?? again. The impact is in 2 minutes now. You do not even know what is going to hit the Valkyria, but all you know is that you have to flee. You were prepared for this in your training.""")


    return name,shipname

def faststart():
    name = str(input(""))
    shipname = str(input(""))
    return name,shipname
print(colorstring("aaa","PURPLE"))
print(colorstring("aaa","BLUE"))
print(colorstring("aaa","CYAN"))
print(colorstring("aaa","GREEN"))
print(colorstring("aaa","YELLOW"))
print(colorstring("aaa","FAIL"))
print(colorstring("aaa","BOLD"))
print(colorstring("aaa","UNDERLINE"))


X = Game()
X.start_game()


