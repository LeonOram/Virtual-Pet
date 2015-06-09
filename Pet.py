#class definition
class VirtualPet():
    #constructor
    def __init__(self,name):
        self.name = name
        self.size = 0
        self.age = 0
        self.energy = 50
        self.hunger = 50
        self.thirst = 50
        self.tired = 50
        self.size = 50
        self.feeds = 0
        self.mood = 50
        self.foods=["stuff","bob"]
        print("I have been born")

    def eat(self,food):
        if self.feeds < 5:
            if self.hunger < 95:
                if food[0] in self.foods:
                    print("Nom")
                    self.hunger = self.hunger + food[1]
                    self.mood = self.mood + 7
                    self.feeds = self.feeds + 1
                    if self.hunger > 100:
                        self.hunger = 100
                else:
                    print("Not eating that!")
                    self.mood = self.mood - 5
            else:
                print("Too full")
        else:
            print("Nope not again")

    def sleep(self,length):
        if length > 0:
            if length < 8:
                print("ZZZZzzzz")
                self.feeds = 0
                self.hunger = self.hunger - 20
                self.tired = self.tired + length*10
                if self.tired > 100:
                    self.tired = 100
            else:
                print("I'm not sleeping that long!")
        else:
            print("Thats not a sleep")


food_list=[["Pizza",10],["bob",25]]
#create instance
pet_one = VirtualPet("Steve")

#Menu
def display_main_menu():
    print('''
--Main Menu--
1. View Stats
2. Feed
3. Sleep
''')

def get_main_menu_selection():
    options = [1,2,3]
    selection = int(input(""))
    if selection in options:
        if selection == 1:
            display_stats()
        elif selection == 2:
            pet_feed()
        elif selection == 3:
            pet_sleep()

def display_stats():
    pass

def pet_eat():
    print("Foods")
    for food in food_list:
        print(food[0],"   ",food[1])
    selection = int(input(""))
    if selection > 0 and selection < len(food_list):
        

    
def pet_sleep():
