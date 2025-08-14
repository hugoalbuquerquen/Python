import os
import sys

class CPU_emulator:
    def __init__(self):

        print("")
        self.user_name = input("Hi! What's your name? ").upper()
        print("")
        
        memory_size = ""
        while(not memory_size.isdigit()):

            os.system('cls' if os.name == 'nt' else 'clear')

            print("")
            print("Welcome! {}".format(self.user_name))
            print("")

            try:
                memory_size = int(input("What's your memory size? "))
            except:
                memory_size = ""
            else:
                break

        
        self.memory = {}
        
        #registers will be a 4th of the capacity of the memory ('cause I want to :P
        self.reg_size = memory_size // 4
        self.registers = {}
        self.reg_idx = 1

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            print("")
            print("Welcome, {}!".format(self.user_name.upper()))
            print("")

            print("'END' - To finish the program.")
            print("'INSERT int' - To insert value into registers.")
            print("'STORE Rn $n' - To save a value from a register into the memory.")
            print("'LOAD Rn $n' - To fectche a value from memory into a register.")
            print("'ADD/SUB/MUL/DIV Rn Rn' - To update the first Rn with the result.")
            print("")

            
            
            print("Register: {}/{} - {}".format(len(self.registers), self.reg_size, self.registers))
            print("Memory: {}/{} - {}".format(len(self.memory), memory_size, self.memory))
            print("")

            self.fetch_data(input().upper().split())

    def fetch_data(self, data):

        if(len(data) <= 0):
            return
        
        elif(len(data) <= 1):

            if(data[0] == "END"):
                print("\nGoodbye {}!\n".format(self.user_name))
                sys.exit()
        
        elif(len(data) <= 2):

            if(data[0] == "PRINT"):
                self.print_data(data[1])
            
            elif(data[0] == "INSERT"):
                #insert_data(value):
                self.insert_data(data[1])
            
            else:
                return 
        
        else:

            if(data[0] == "STORE"):
                #store_data(reg_address, memo_address):
                self.store_data(data[1], data[2])

            elif(data[0] == "LOAD"):
                #load_data(reg_address, memo_address)
                self.load_data(data[1], data[2])

            elif(data[1] in self.registers and data[2] in self.registers):

                if(data[0] == "ADD"):
                    self.add(data[1], data[2])
                    
                elif(data[0] == "SUB"):
                    self.sub(data[1], data[2])

                elif(data[0] == "MUL"):
                    self.mul(data[1], data[2])

                elif(data[0] == "DIV"):
                    self.div(data[1], data[2])
            
            else:
                return

    ###############################  FUNCTIONS  ###############################

    def update_idx(self, reg_address=None):

        if(reg_address is not None):
            self.reg_idx = list(self.registers).index(reg_address) + 1

        if(self.reg_idx == self.reg_size):
            self.reg_idx = 1
        
        else:
            self.reg_idx += 1


    def print_data(self, address):

        if(address in self.registers):
            print(self.registers[address])
        
        elif(address in self.memory):
            print(self.memory[address])

        else:
            return


    def insert_data(self, value):

        try:
            value = float(value) * 1.0
        except:
            return
        else:
            reg_address = "R" + str(self.reg_idx)

            self.update_idx()

            if(len(self.registers) < self.reg_size or reg_address in self.registers):
                self.registers[reg_address] = value
            else:
                return
    

    def store_data(self, reg_address, memo_address):

        if(memo_address.count("$") == 1 and memo_address[0] == "$" and 
                len(memo_address) >= 2 and (memo_address.strip("$").isdigit()) and
                int(memo_address.strip("$")) >= 0 and reg_address in self.registers and
                (memo_address in self.memory or len(self.memory) < 8)):
            self.memory[memo_address] = self.registers[reg_address]

        else:
            return
    

    def load_data(self, reg_address, memo_address):

        if(reg_address in self.registers and memo_address in self.memory):
            self.registers[reg_address] = self.memory[memo_address]

        else:
            return
    


    def add(self, address_1, address_2):
        self.update_idx(address_1)
        self.registers[address_1] = self.registers[address_1] + self.registers[address_2]

    def sub(self, address_1, address_2):
        self.update_idx(address_1)
        self.registers[address_1] = self.registers[address_1] - self.registers[address_2]
    
    def mul(self, address_1, address_2):
       self.update_idx(address_1)
       self.registers[address_1] = round((self.registers[address_1] * self.registers[address_2]), 2)

    def div(self, address_1, address_2):

        if(self.registers[address_2] == 0):
            print("Can't divide by 0.")
            return
        
        else:
            self.update_idx(address_1)
            self.registers[address_1] = round((self.registers[address_1] / self.registers[address_2]), 2)

my_cpu = CPU_emulator()
