# Name: Jadyn Kennedy
# Date: 2/5/2020
# Citations: Used the template provided on iLearn, and past labs for refrence (otherwise I worked alone)

def main():
    e = "Press enter to continue..."
    g = "GPA:"
    name = input("Please enter your name: ")
    year = input("Please enter what year you are (freshman/sophomore/junior/senior")
    
    print('Help the STEM major find her motivation!')

               
    print()
    print("Welcome to", year," orienation", name, "! You begin your", year, " year, ready and eager to learn!")
    print(g, 4.0)
    input(e)
    print("... Two weeks later ...")
    
    
    print("Oh no! You can't seem to find your motivation to continue! Where should you look?")
    input(e)
    print("You look through all the drawers in your room, making a mess in the process. There's nothing here.",
          "You know you have a",
          "project due in your Programming class in an hour, but you decide to clean up your mess instead.")

   
    print("You were late to class... with an incomplete project.")
    print(g, 3.5)
    input(e)

    print("Congratulations,", name, "! After your teacher scolded you for your project, you",
          "found a pinch of motivation on the floor and finally finish that project!",
          "You turn it in 2 days late and luckily your teacher takes pity",
          "on you and accepts it.")
    print(g, 3.8)
    input(e)

    print("You feel relieved to see your grades back up and decide to give yourself a nice break as a reward",
          "so you decide to skip your classes for the next day.")
    print(g, 3.0)
    input(e)



    print("You start seeing assignments pile up in your peripheral vision as you watch netflix. You know you",
          "should start them, but your motivation has once again run out.")
    input("Press enter to look for some more!")
    print("As you look start searching, you come across an email saying: '", name,", Don't forget to keep your",
          "grades up so you don't lose your full ride scholarship.'")
    input(e)
    print("Congratulations! That should be enough motivation to last you",
          "untill you graduate!")
    input(e)
    print("You power through all of your assignments and finish your", year, "year strong.")
    print(g, 4.0)

    print("You have won! Please play again!")


main()
