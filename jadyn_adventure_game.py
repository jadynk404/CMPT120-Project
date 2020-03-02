# Name: Jadyn Kennedy
# Date: 2/10/2020
# Citations: Worked with Emmanuel Batista for Project 1, this time I worked alone. 


e = ("Press enter to continue...")
g = ("GPA:")
gpa = float(4.0)
name = input("Please enter your name: ")
year = input("Please enter what year you are (freshman/sophomore/junior/senior): ")
invalid = "I'm sorry. That is not a valid command."


locales = ["You decide to head outside to look for some motivation. The fresh summer air hits you and you realize today is going to be a good day."\
           "You do all of your homework outside and get all your assignments done.", "You decide to head to the library to look. All of the studious people"\
           "surrounding you seemed to spark some motivation. Not only did you finish all of todays work,"
           " but everything for the next week too! Congratulations!", "You decide to look for some motivation under your bed, but you found"\
           "some extra pillows and blankets that you have stored instead. You decide to look for your motivation later and take a nap instead, ignoring your"\
           "assignments.", "You try looking for some motivation at the gym. Luckily you found some but you spent all of it working out instead of doing your work!",\
           "You try looking for your motivation in your room. Congratulations! You find some hiding under the giant pile of assignments you have due!"\
           "You get to work and finish all of them with time to spare!", "You head to Hancock to try to find some motivation. Struggling, you "\
           "decide to stop for a nice cup of coffee. As you drink it you remember that you have a Programming project due in an hour! You finish 3/4 "\
           "of it while you finish your coffee."]
current = locales[0]





       

import time
import sys

def main(function):   #added parameter          
    function()

def copyright(variable):
    print(variable)
def Intro():
    p1 = 'Help the STEM major find her motivation!'
    Quit = "(Press quit at any time to exit the game.)"
    p2 = "Welcome to {} orientation, {}! You begin your {} year, ready and eager to learn!".format(year, name, year) #This fixes the formatting of text
    p3 = "... Two weeks later ..."
    p4 = "Oh no! You can't seem to find your motivation to continue!"
    print(p1)
    print(Quit)
    print() # print blank space
    time.sleep(1)

    print(p2)
    print(p3)
    print(p4)

def local1():
    current = locales[0]
    print(current)
    print(g, gpa)
    print(e)
def local2():
    current = locales[1]
    print(current)
    print(g, gpa)
    print(e)
def local3():
    current = locales[2]
    print(current)
    print(g, gpa-1.0)
    print(e)
def local4():
    current = locales[3]
    print(current)
    print(g, gpa-.5)
    print(e)
def local5():
    current = locales[4]
    print(current)
    print(g, gpa)
    print(e)
def local6():
    current = locales[5]
    print(current)
    print(g, gpa-.15)
    print(e)

def loop():
    x = 1
    while x ==1:
        prompt = "Where would you like to look?\n"
        choice = input(prompt)
        invalid = "That is not a valid command. Enter 'help' for help"
        Help = "Please suggest either north, south, east, west, or quit.\n"
        north = "You go north."
        south = "You go south."
        east = "You go east."
        west = "You go west."
        if choice[0] == "h":
           x = 1
           print(Help)
        elif choice[0] == "q":
           x = 0
           Quit()
        elif choice[0] == "n" or choice[0] == "s" or choice[0] == "e" or choice[0] == "w":
            x = 1
            if current == locales[0]:
                x=1
                if choice[0] == "n":
                    x = 1
                    local3()
                elif choice[0] == "e":
                    x=1
                    local2()
                elif choice[0] == "w":
                    x=1
                    local1()
                if choice[0] == "s": 
                    x=1
                    print(invalid)
            elif current == locales[1]:
                if choice[0] == "n":
                    x = 1
                    local4()
                elif choice[0] == "e":
                    x=1
                    print(invalid)
                elif choice[0] == "w":
                    x=1
                    local0()
                if choice[0] == "s": 
                    x=1
                    print(invalid)
            elif current == locales[2]:
                x=1
                if choice[0] == "n":
                    x = 1
                    local5()
                elif choice[0] == "e":
                    x=1
                    local1()
                elif choice[0] == "w":
                    x=1
                    print(invalid)
                if choice[0] == "s": 
                    x=1
                    print(invalid)
            elif current == locales[3]:
                x=1
                if choice[0] == "n":
                    x = 1
                    local6()
                elif choice[0] == "e":
                    x=1
                    local4()
                elif choice[0] == "w":
                    x=1
                    print(invalid)
                if choice[0] == "s": 
                    x=1
                    local0()
            elif current == locales[4]:
                x=1
                if choice[0] == "n":
                    x = 1
                    print(invalid)
                elif choice[0] == "e":
                    x=1
                    print(invalid)
                elif choice[0] == "w":
                    x=1
                    local3()
                if choice[0] == "s": 
                    x=1
                    local1()
            elif current == locales[5]:
                x=1
                if choice[0] == "n":
                    x = 1
                    print(invalid)
                elif choice[0] == "e":
                    x=1
                    print(invalid)
                elif choice[0] == "w":
                    x=1
                    local6()
                if choice[0] == "s": 
                    x=1
                    local2()
                    
                  
        else:
            x=1
            print(invalid)
           


def Quit():
    print("ok. goodbye")
    

def main():
    c = "This game was created by Jadyn Kennedy 2/10/2020" # copyright
    Intro()
    loop()
    copyright(c)
    


main()
