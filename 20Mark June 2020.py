#      Q05

def displayMenu():
     # Completed subprogram that displays the menu
    
    print("                  Menu                    ")
    print("------------------------------------------")
    print("[1] Add player name")
    print("[2] Play guess the capital city")
    print("[3] End game")
    print("------------------------------------------")

def getMenuChoice():
    # Completed subprogram that gets and validates the menu choice
    choices = [1,2,3]
    mChoice = 0
    
    # Menu choice is validated
    while mChoice not in choices:
        mChoice = int(input("Input your menu choice: "))

    # Valid menu option returned to the main menu
    return mChoice
     
def addPlayerName(fplayerName):
    # Add your code to:
    #   ensure a player name is input
    #   return the player name to the main menu

    while fplayerName == "":
        fplayerName = input("Input your name: ")

    return  fplayerName


def guessCapital():
    # Partially completed subprogram to:
    #   display questions
    #   check guesses
    #   return final score
    
    # Arrays holding question numbers, countries and their capital cities
    questions = [1,2,3,4,5,6,7,8,9]
    countries = ["England","France","Spain","Italy","Germany","Scotland","Wales","United Arab Emirates","China"]
    capitals = ["London","Paris","Madrid","Rome","Berlin","Edinburgh","Cardiff","Abu Dhabi","Beijing"]

    questionCount = 1
    questionScore = 0

    # Add your code here


     #A while loop to make sure the code runs until 5 questions filled in
    while questionCount != 6:
          #Creates a array to store the vaalible questions
        avalibleQuestions = [] 
        questionSelect = -1
          
          #Adds the valid questions to the avalible questions array to later print to theu ser
        for x in questions:
            if x != 0:
                avalibleQuestions.append(x)
          
          #Print out the questions
        print("The questions area: ", avalibleQuestions)
        print("\n")
          
          #Validation uses to make sure user selects a valid one
        while questionSelect not in avalibleQuestions:
            questionSelect = int(input("Select a question: "))
          #Print question and accept input
        print("What is the capital of " + countries[questionSelect - 1] + "?")
        answer = input(": ")

               # .upper validation to prevent London/london/LONdon from not being accepted
        if answer.upper() == capitals[questionSelect - 1].upper():
            print("That is correct! ")
            questionScore += 1
        else:
            print("That is wrong the capital of " + countries[questionSelect - 1] + " is " + capitals[questionSelect - 1]  )
          
          #New line formating
        print("\n")
         #Set question to 0 so it WILL never be reused 
          #More effcient then removing array elemnts as it can get messy on long lists
        questions[questionSelect - 1] = 0

          
        questionCount += 1



    return questionScore

menuChoice = 0
score = 0
playerName = ""

while menuChoice != 3:
    displayMenu()
    menuChoice = getMenuChoice()


    # Add your code to:
    #   call the relevant subprogram if the menu choice is 1 or 2
    #   display the player name and the score if the menu choice is 3

    if menuChoice == 1:
        playerName = addPlayerName(playerName)
    elif menuChoice == 2:
        score = guessCapital()

        

print("Player name: " + playerName + "  Your final score is: " + str(score))
