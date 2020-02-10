# Name: Jadyn Kennedy
# Date: 2/10/2020
# Citation: resources on iLearn, Emmanuel Batista

def copyright(variable):
    print(variable)
    

def print1():
    p1 = 'Help the STEM major find her motivation!'

    print(p1)
    print() # print blank space 

    e = ("Press enter to continue...")
    g = ("GPA:")
    gpa = float(4.0)
    name = input("Please enter your name: ")
    year = input("Please enter what year you are (freshman/sophomore/junior/senior): ")
    p2 = "Welcome to {} orienation,{}! You begin your year year, ready and eager to learn!".format(year, name) #this fixes the format 
    p3 = "... Two weeks later ..."
    p4 = "Oh no! You can't seem to find your motivation to continue! Where should you look?"
    p5 ="You look through all the drawers in your room, making a mess in the process. There's nothing here. You know you have a project due in your Programming class in an hour, but you decide to clean up your mess instead."
    p6 = "You were late to class... with an incomplete project."
    p7 = "Congratulations,{}! After your teacher scolded you for your project, you found a pinch of motivation on the floor and finally finish that project! You turn it in 2 days late and luckily your teacher takes pity on you and accepts it.".format(name)
    p8 = "You feel relieved to see your grades back up and decide to give yourself a nice break as a reward so you decide to skip your classes for the next day."
    p9 = "You start seeing assignments pile up in your peripheral vision as you watch netflix. You know you should start them, but your motivation has once again run out."
    p10 = "Press enter to look for some more!"
    p11 = "As you look start searching, you come across an email saying: '{}', Don't forget to keep your grades up so you don't lose your full ride scholarship.'".format(name)
    p12 = "Congratulations! That should be enough motivation to last you until you graduate!"
    p13 = "You complete all of your assignments and finish the semester strong."
    p14 = "You have won! Please play again!"
   

    

    
    print()
    print(p2)
    print(g, gpa)
    input(e)
    print(p3)

    print(p4)
    input(e)
    print(p5)

    print(p6)
    print(g, gpa-.5)
    input(e)

    print(p7)
    print(g, gpa-.2)
    input(e)

    print(p8)
    print(g, gpa-1.0)
    input(e)

    print(p9)
    input(p10)
    print(p11)
    input(e)
    print(p12)
    input(e)
    print(p13)
    print(g, gpa)

    print(p14)
    


    
def main():
    print1()

    c = "This game was created by Jadyn Kennedy 2/10/2020" # copyright
    copyright(c)

    



main()
    
    


