#Worked with Emmanuel Batista

def main():
    title = "Interactive Dictionary"
    print(title)
    myFile = input("Please input the name of your file: ").strip()
    myFile = myFile.lower()

    with open(myFile, "r") as myFile: #reads file and assigns value to variables
        dictionary = myFile.readlines()
        word1 = dictionary[0].strip()
        def1 = dictionary[1].strip()
        word2 = dictionary[2].strip()
        def2 = dictionary[3].strip()
        inDictionary = {
            word1 : def1,
            word2 : def2
        }
    
    x = 1
    while x==1: #searches txt file for user input
        uinput = "Please input a word you would like to have defined: "
        prompt = input(uinput).strip()
        prompt = prompt.lower()
        if prompt == word1:
            print(inDictionary[word1])
        elif prompt == word2:
            print(inDictionary[word2])
        elif prompt == "":
            x = 0 
        else:
            invalid = "I'm sorry. This word is not stored in our dictionary."
            print(invalid)
            x = 1

    def copyrightt():
        c = "This file was created by Jadyn Kennedy 4/27/2020"

main()
copyrightt()
 
