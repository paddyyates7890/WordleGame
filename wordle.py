from tkinter import S
import emoji

def game(word = str):
    squareList = []
    gueses = 6
    print("WELCOME TO WORDLE")
    print("The game is simple guess a word and press enter \nif any letters in the word are correct the will show up with a green square \nif theay are correct but in the wrong place a yellow \nif wrong it will stay white ")
    print("you only get 6 gueses")
    print("")
    
    for i  in range(len(word)):
        print(emoji.emojize("  :red_square:"), end = "")
        
    while (True):
        green = False
        yellow = False
        correct = False
        print("\nenter your guess length is ",len(word))
        guess = input()
    
        if (guess == word):
            win(word)
            break
        elif (gueses < 7):
            for i in range(len(guess)):
                for j in range(len(word)):
                    if (guess[i] == word[j] and i == j):
                        green = True
                    elif (guess[i] == word[j] and i != j):
                        yellow = True
                        
                    if (green == True):
                        print(emoji.emojize("  :green_square:"), end = "")
                        green = False
                        correct = True
                    elif (yellow == True):
                        print(emoji.emojize("  :yellow_square:"), end = "")
                        yellow = False
                        correct = True
                        
                if (correct != True):
                    print(emoji.emojize("  :red_square:"), end = "")
                else:
                    correct = False
             
        else:
            loose(loose)
            break
    
    
def win(word = str):
    print("we done you have won the game")
    for i  in range(len(word)):
        print(emoji.emojize("  :green_square:"), end = "")

def loose():
    print("unlucky too many guesses")
    
if  __name__ == "__main__":
    word = "computing"
    game(word)
    