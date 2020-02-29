# Name: Jadyn Kennedy
# Date: 2/10/2020


e = ("Press enter to continue...")
g = ("GPA:")
name = input("Please enter your name: ")
year = input("Please enter what year you are (freshman/sophomore/junior/senior): ")
invalid = "I'm sorry. That is not a valid command."


import time
import sys



             
def someFunc(function):   #added parameter          
    function()

def copyright(variable):
    print(variable)


def Quit():
    print("ok. goodbye")
    sys.exit()
    
def loop():
    x = 1
    while x == 1:
        prompt = "Where would you like to go from here?\n"
        choice = input(prompt)
        invalid = "That is not a valid command. Enter 'help' for help"
        Help = "Please suggest either north, south, east, west, or quit.\n"
        north = "you go north"
        south = "you go south"
        east = "you go east"
        west = "you go east"
        
        
        

        choice = choice.lower()
        if choice[0] == "n":
            x = 0
            print(north)

        elif choice[0] == "s":
            x = 0
            print(south)
        elif choice[0] == "e":
            x = 0
            print(east)

        elif choice[0] == "w":
            x = 0
            print(west)
        elif choice[0] == "h":
            x = 1
            print(Help)
        elif choice [0] == "q":
            Quit()
        else:
            x = 1
            print(invalid)
            

    
    return loop



def Intro():
    p1 = 'Help the STEM major find her motivation!'

    print(p1)
    print() # print blank space
    time.sleep(1)

    
    p2 = "Welcome to {} orientation, {}! You begin your {} year, ready and eager to learn!".format(year, name, year) #This fixes the formatting of text
    p3 = "... Two weeks later ..."

    

    
    print()
    print(p2)
    print(g, 4.0)
    input(e)
    print(p3)

def printsub1():
    p4sub1 = "Oh no! You can't seem to find your motivation to continue!"
    print(p4sub1)

def print1():
    x = 1
    while x==1:
        
        p4 = "Where should you look: through your drawers or in the closet?\n"
        p51 ="You look through all the drawers in your room, making a mess in the process. There's nothing here." 
        p52 = "Your scavenge through your closet, throwing all of your clothes onto the floor. There's nothing here." 
        suggest1 = "Please suggest either drawers or closet.\n"
        choice1 =input(p4)

        choice1 = choice1.lower()

        if choice1[0] == "d":
            x = 0
            print(p51)
        elif choice1[0] == "c":
            x = 0
            print(p52)

            
        else:
            print(invalid)
            tryagain = input(suggest1)
            tryagain = tryagain.lower() #allows reader to input capital or lower case answers
            if tryagain[0] == "d":
                x = 0
                print(p51)
            elif tryagain[0] == "c":
                x = 0
                print(p52)
            else:
                x=1
                
            
    
        input(e)

def printincomplete():
    p6 = "You were late to class... with an incomplete project."
   

    print(p6)
    print(g, 3.5)
    input(e)


def printwork():
    work = "You made it to class with a half finished project." 

    print(p6)
    print(g, 3.7)
    input(e)

    
def print2():
    x = 1
    while x==1:
        project = "You have your Computer Programming game due in an hour and you haven't started it yet but your roommate has already yelled at you twice this week to clean the room. Do you try to work on it or clean up the mess you made before your roommate gets home?\n"
        suggest2 = "Please suggest either clean or work.\n"
        choice2 = input(project)

        choice2 = choice2.lower()
        if choice2[0] == "c":
            x = 0
            printincomplete()

        elif choice2[0] == "w":
            x = 0
            printwork()

        
        else:
            x = 1
            
            tryagain = input(suggest2)
            tryagain = tryagain.lower()
            if tryagain[0] == "w":
                x = 0
                print(printwork)
            elif tryagain[0] == "c":
                x = 0
                print(printincomplete)
            else:
                x = 1
            



def print3():

    p8 = "You feel relieved to see your grades back up and decide to give yourself a nice break as a reward so you decide to skip your classes for the next day."
    p9 = "You start seeing assignments pile up in your peripheral vision as you watch netflix. You know you should start them, but your motivation has once again run out."
    

    print(p8)
    print(g, 3.0)
    input(e)

    print(p9)
    loop()

def print4():
    p11 = "As you look start searching, you come across an email saying: '{}, Don't forget to keep your grades up so you don't lose your full ride scholarship.'\n".format(name)
    p12 = "Congratulations! That should be enough motivation to last you until you graduate!"
    p13 = "You complete all of your assignments and finish the semester strong."

    print(p11)
    print(p12)
    input(e)

def print5():
    print(p13)
    print(g, 4.0)

def print5():
    p14 = "You have won! Please play again!"

    print(p14)

    
def main():

        someFunc(Intro)
        someFunc(printsub1) 
        someFunc(print1)
        someFunc(print2)
        someFunc(print3)
        someFunc(print4)
        someFunc(print5)

#To do: Add two more locals, create choices for each local, change the GPA depending on which route taken


    

main()
    
    




