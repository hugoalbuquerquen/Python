import os
class Player:

    def __init__(self):
        self.name = input("What's your name?")
        print ("Player 1 : ", self.name)
        self.ships_dic = {}


class Ship:

    os.system('cls' if os.name == 'nt' else 'clear')

    ships_dic = {}
    bombing_dic = {}
    battle_map = ""
    #{2:["D3", "E3"], 3:["E3", "E4", "E5"], 5:["A5", "B5", "C5", "D5", "E5"]}
    field_columns = "\t  A   B   C   D   E   F   G   H   I"
    field_rowns = "123456789"

    def __init__(self):
        self.length = 0
        Ship.print_map(self, False)
        
    def print_map(self, hit):
    
        print("Welcome to Battleship V 1.3")
        print("\n\t--- INSTRUCTIONS ---\n\nEach player has 4 ships. \nEach measuring 2, 3, 4 and 5 squares. \nShips can only be placed horizontally or vertically.\n")
        
        Ship.battle_map = self.field_columns
        #print(self.field_columns)
        for l in range(1, 10):
            line = " "
            col = ""
            for c in range(9):
                line +=  "--- "

                temp = str(chr(c+65) + str(l))
                if(temp in Ship.bombing_dic.keys()):
                    if (Ship.bombing_dic.get(temp)):
                        col += "| {hit} ".format(hit="X")
                    else:
                        col += "| {hit} ".format(hit="~")
                else:
                    col += "| {hit} ".format(hit=" ")

            Ship.battle_map += "\n\t" + line
            #print("\t" + line)
            col += "| " + str(l)
            
            #print("\t" + col)
            Ship.battle_map += "\n\t" + col
        
        Ship.battle_map += "\n\t" + line
        #print("\t" + line)
        print(Ship.battle_map)
        print("\n")

        if (len(self.ships_dic.values()) > 0):
            for k, v in self.ships_dic.items():
                print(k, v)
            print("\n")
        
    def read_coord(self, flag_bomb):

        coord = ""
        while(len(coord) != 2 or coord[0] not in self.field_columns or coord[1] not in self.field_rowns):
            
            os.system('cls' if os.name == 'nt' else 'clear')
            Ship.print_map(self, False)

            if (not flag_bomb):
                print("\t{len} squares ship details\n".format(len=self.length))
            else:
                print("\tTime to drop BOMBS!!!\n")

            coord = input("Coordinates (Column Row - 'CR'): ").upper()
        
        return coord
    

    def read_direction(self):
        direction = ""
        while (direction != "H" and direction != "V"):
            
            coord = Ship.read_coord(self, False)

            #print("Starting coordinates (Column Row - 'CR'): {st}".format(st=start))
            direction = input("Use 'H'-Horizontal or 'V'-Vertical. Direction: ").upper()
        
        return coord, direction

    
    def create_ship(self, length):

        self.length = length
        ship_coordinates = []
        
        while (len(ship_coordinates) != self.length):

            start_coord, direction = Ship.read_direction(self)
            
            coordinate = ""
            if (direction == "V"):
                for i in range(0, length):
                    coordinate = start_coord[0] + "" + str(int(start_coord[1]) + i)
                    ship_coordinates.append(coordinate)
            
            else:
                for i in range(0, length):
                    coordinate = chr(ord(start_coord[0]) + i) + "" + start_coord[1]
                    ship_coordinates.append(coordinate)


            #print(ship_coordinates)  
            for c in ship_coordinates:
                if len(c) != 2 or c[0] not in self.field_columns or c[1] not in self.field_rowns:
                    ship_coordinates.clear()                        

                else:
                    for val in Ship.ships_dic.values():
                        if c in val:
                            #print("Invalid {pos}. No parts of two ships can be in the same square.".format(pos=c))
                            ship_coordinates.clear()
                            break
        
        Ship.ships_dic[length] = ship_coordinates

    
    def input_attack(self):
        
        hit = True

        while (hit):
            
            coord = Ship.read_coord(self, True)

            if (coord in Ship.bombing_dic.keys()):
                break

            else:
                for val in Ship.ships_dic.values():
                    if coord in val:
                        hit = True
                        val.remove(coord)
                        #print("HIT")

                        if (len(val) == 0):
                            #print(key, "squares ship has been destroyed.")
                            val.append("DESTROYED")
                            #Ship.ships_dic.pop(key)

                        break
                    else:
                        hit = False                
                
                Ship.bombing_dic[coord] = hit
                Ship.print_map(self, hit)

                if (not hit):
                    #print("WATER")
                    hit = True

            """if (len(Ship.bombing_dic.values() == True) == 6):
                Ship.print_map(self, False)
                print("\n\tGAME OVER\n")
                hit = False"""



player1 = Ship()
player1.create_ship(2)
#player1.create_ship(3)
player1.create_ship(4)
#player1.create_ship(5)

player2 = Ship()
player2.input_attack()