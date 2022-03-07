# Modules 
import requests, json, time, random

# Key 
API_Key = '9ffe7824-919f-4a62-81fa-7746f1ff770f' 

# URL
cat_url = 'https://api.thecatapi.com/v1/breeds?key=' + API_Key  # authenticate the url with my key

# Call API 
response = requests.get(cat_url) 
response.raise_for_status() # check for errors

# Load JSON data into a Python variable 
jsonData = json.loads(response.text)

# Functions  
def searchCatBreeds(numberofCats):
    numberofCats = float(input("How many cats do you want (pick a number between 1 and 60.)")) # user decdies how many cats they want to make
    named_cats = [] # stores cat breeds user gets 
    while numberofCats != 0: # continues until number of cats user wants is 0
        for cats in jsonData: # iterates over JSON dictionary
            nameofCat = input("What is the name of this cat?")
            cat_breed = jsonData[random.randint(0,65)]["name"] # collects random cat breed from the dictionary
            
            print("This is " + nameofCat + ".  It is a "  + cat_breed +  ".  How puurfect.")
            named_cats.append(cat_breed)  
            break # terminates for loop so that while condition can be checked
        numberofCats = numberofCats - 1 # subtracts a cat from user wanted number
    
    # Asks user to see if they want to see their breeds of cats
    see_cats = input("Want to see the breeds of your cat? (y or n)")
    if see_cats == "y" or see_cats == "Y":
        print("Your breeds are: " + str(named_cats)) # shows breeds of cats
    elif see_cats == "n" or see_cats == "N":
        print("Understood")
    else:
        print("Choose y or n")
    return numberofCats
    

def isCatFriendly(numberofCats):
    numberofCats = float(input("How many cats do you want (pick a number between 1 and 60.")) 
    evil_cat = [] 
    good_cat = []
    cat_loves_stranger = []
    cat_loves_dog = [] 
    cat_loves_kid = []
    while numberofCats != 0: # terminates once number of cats people want is 0
        for cats in jsonData: 
            nameofCat = input("Name your cat.") # user names their cat
            cat_stranger_nice = jsonData[random.randint(0,65)]["stranger_friendly"] 
            cat_dog_nice = jsonData[random.randint(0,65)]["dog_friendly"]
            cat_child_nice = jsonData[random.randint(0,65)]["child_friendly"] # collects dictionary values from these keys
            if cat_stranger_nice < 3 and cat_dog_nice < 3 and cat_child_nice < 3: # for worst cats that aren't nice to anyone
                print(nameofCat + " is not very nice. Grrrr")  
                evil_cat.append(nameofCat)
            elif cat_stranger_nice >= 3 and cat_dog_nice >= 3 and cat_child_nice >= 3: # for best behaved cats who like everyone
                print(nameofCat + " is a darling and loves everyone")
                good_cat.append(nameofCat) # kindest cats go to good cat list; logic follows for rest of the statements
            elif cat_dog_nice >= 3:
                print(nameofCat + " likes dogs!")  
                cat_loves_dog.append(nameofCat)
            elif cat_child_nice >= 3:
                print(nameofCat + " is child safe!")  
                cat_loves_kid.append(nameofCat)
            else:
                print(nameofCat +  " can be tempermental, but he cares!")  
            break # terminates loop so that while loop can be updated
        numberofCats = numberofCats - 1    # updates while condition for each new cat
    
    # Looks up lists of different cats
    see_cat_morality = input("Want to see evil cats (e), good cats (g), stranger-liking cats (s), dog-liking cats (d), or kid-liking cats (k)") # asks users to see different lists of cats
    if see_cat_morality == 'e' or see_cat_morality == 'E':
        print("These kitties are up to no good: " + str(evil_cat)) # prints list of cats that hates everyone; logic follows for rest
    elif see_cat_morality == 'g' or see_cat_morality == 'G':
        print("These kitties are angels :D" + str(good_cat)) 
    elif see_cat_morality == 's' or see_cat_morality == 'S':
        print("These kitties love strangers" + str(cat_loves_stranger))
    elif see_cat_morality == 'd' or see_cat_morality == 'D':
        print("These kitties don't mind a smelly dog" + str(cat_loves_dog))
    elif see_cat_morality == 'k' or see_cat_morality == 'K':
        print("These kitties are certified babysitters" + str(cat_loves_kid))
    return numberofCats 


# Main 
Game = True
while Game is True:   # Runs through code as long as game condition is true 
    numberofCats = '' # initialize number of cats variable

    # Decides which part of the program the user wants to do
    decision = input("What do you want to learn? Want to search a cat breed (c) or see if a cat is friendly (f)?")
    if decision == 'c' or decision == 'C':
        searchCatBreeds(numberofCats)  
    elif decision == 'f' or decision == 'F':
        isCatFriendly(numberofCats) 
    else:
        print("Choose c or f")

    # See if user likes the program
    user_like = input('Did you like this program?')
    time.sleep(1) # suspense 0_0
    print('Good')  

    # Asks user if they wish to continue the game
    play_again = input("Want to continue looking through the data (y) or (n)?") 
    if play_again == "y" or play_again == "Y":
        Game = True 
    else:
        Game = False 
  



