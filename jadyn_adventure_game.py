# Name: Jadyn Kennedy
# Date: 3/3/2020
# Citations: Worked with Emmanuel Batista (helped me with the "global current" and understanding that functionality), otherwise I worked alone

#global variables:
e = ("Press enter to continue...")
g = ("GPA:")
gpa = float(4.0)
name = input("Please enter your name: ")
year = input("Please enter what year you are (freshman/sophomore/junior/senior): ")
invalid = "I'm sorry. That is not a valid command."

#global list:
locales = ["You decide to head outside to look for some motivation. The fresh summer air hits you and you realize today is going to be a good day. "\
           "You do all of your homework outside and get all your assignments done.", "You decide to head to the library to look. All of the studious people"\
           " surrounding you seemed to spark some motivation. Not only did you finish all of todays work,"
           " but everything for the next week too! Congratulations!", "You decide to look for some motivation under your bed, but you found"\
           " some extra pillows and blankets that you have stored instead. You decide to look for your motivation later and take a nap instead, ignoring your"\
           " assignments.", "You try looking for some motivation at the gym. Luckily you found some but you spent all of it working out instead of doing your work!",\
           "You try looking for your motivation in your room. Congratulations! You find some hiding under the giant pile of assignments you have due!"\
           " You get to work and finish all of them with time to spare!", "You head to Hancock to try to find some motivation. Struggling, you "\
           "decide to stop for a nice cup of coffee. As you drink it you remember that you have a Programming project due in an hour! You finish 3/4 "\
           "of it while you finish your coffee."]

#new global list:
locNames = ["Outside", "The Library", "Under the Bed", "The Gym", "Your room", "Hancock"]

#tracking where the player has been:
hasBeen = [False, False, False, False, False, False] 

current = locales[0] #global variable for location (will update in each locale)
clocName = locNames[0] 

       
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
    time.sleep(1) #pauses before printing next line of text

    print(p2)
    print(p3)
    print(p4)


    

def local1():
    global clocName
    global current #this will update the players current location
    global gpa #this will update the players current gpa
    global hasBeen
    if hasBeen[0] == False:
        gpa = gpa+0.15
    else:
        gpa = gpa
    clocName = locNames[0]
    current = locales[0]
    print(clocName)
    print(g, gpa)
    time.sleep(1)
    print(current)
    input(e)
    hasBeen[0] = True #will not change the players gpa if they've already visited the function
    return hasBeen[0]
    
def local2():
    global clocName
    global current
    global gpa
    global hasBeen
    if hasBeen[1] == False:
        gpa = gpa+0.5
    else:
        gpa = gpa
    clocName = locNames[1]
    current = locales[1]
    print(clocName)
    print(g, gpa)
    time.sleep(1)
    print(current)
    input(e)
    hasBeen[1] = True
    return hasBeen[1]

def local3():
    global clocName
    global current
    global gpa
    global hasBeen
    if hasBeen[2] == False:
        gpa = gpa+1.0
    else:
        gpa = gpa
    clocName = locNames[2]
    current = locales[2]
    print(clocName)
    print(g, gpa)
    time.sleep(1)
    print(current)
    input(e)
    hasBeen[2] = True
    return hasBeen[2]
   
def local4():
    global clocName
    global current
    global gpa
    global hasBeen
    if hasBeen[3] == False:
        gpa = gpa-0.5
    else:
        gpa = gpa
    clocName = locNames[3]
    current = locales[3]
    print(clocName)
    print(g, gpa)
    time.sleep(1)
    print(current)
    input(e)
    hasBeen[3] = True
    return hasBeen[3]

def local5():
    global clocName
    global current
    global gpa
    global hasBeen
    if hasBeen[4] == False:
        gpa = gpa+.25
    else:
        gpa = gpa
    clocName = locNames[4]
    current = locales[4]
    print(clocName)
    print(g, gpa)
    time.sleep(1)
    print(current)
    input(e)
    hasBeen[4] = True
    return hasBeen[4]

def local6():
    global clocName
    global current
    global gpa
    global hasBeen
    if hasBeen[5] == False:
        gpa = gpa-0.15
    else:
        gpa = gpa
    clocName = locNames[5]
    current = locales[5]
    print(clocName)
    print(g, gpa)
    time.sleep(1)
    print(current)
    input(e)
    hasBeen[5] = True
    return hasBeen[5]

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
        if choice[0] == "h": #runs help
           x = 1
           print(Help)
        elif choice[0] == "q": #runs quit
           x = 0
           Quit()
        elif choice[0] == "n" or choice[0] == "s" or choice[0] == "e" or choice[0] == "w": #if the player chooses a direction
            x = 1
            if current == locales[0]:
                x=1
                if choice[0] == "n":
                    local4()
                elif choice[0] == "e":
                    local2()
                elif choice[0] == "w":
                    local3()
                elif choice[0] == "s": 
                    print(invalid)
                    
            elif current == locales[1]:
                if choice[0] == "n":
                    local5()
                elif choice[0] == "e":
                    print(invalid)
                elif choice[0] == "w":
                    local1()
                elif choice[0] == "s":
                    print(invalid)
                    
            elif current == locales[2]:
                x=1
                if choice[0] == "n":
                    local6()
                elif choice[0] == "e":
                    local1()
                elif choice[0] == "w":
                    print(invalid)
                elif choice[0] == "s":
                    print(invalid)
                    
            elif current == locales[3]:
                x=1
                if choice[0] == "n":
                    print(invalid)
                elif choice[0] == "e":
                    local5()
                elif choice[0] == "w":
                    local6()
                elif choice[0] == "s": 
                    local1()
                    
            elif current == locales[4]:
                x=1
                if choice[0] == "n":
                    print(invalid)
                elif choice[0] == "e":
                    print(invalid)
                elif choice[0] == "w":
                    local4()
                elif choice[0] == "s": 
                    local2()
                    
            elif current == locales[5]:
                x=1
                if choice[0] == "n":
                    print(invalid)
                elif choice[0] == "e":
                    local4()
                elif choice[0] == "w":
                    print(invalid)
                elif choice[0] == "s": 
                    local3()
                    
                  
        else: #prints invalid if the player gives invalid input
            x=1
            print(invalid)
           


def Quit():
    global gpa
    final = "As you wrap up the year, your final GPA is {}. Have a great summer!".format(gpa)
    print(final)
    

def main():
    c = "This game was created by Jadyn Kennedy 2/10/2020" # copyright
    Intro()
    loop()
    copyright(c)
    


main()
