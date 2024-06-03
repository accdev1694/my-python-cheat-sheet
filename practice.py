import random
# guess word
# player guess a letter in word
# if letter in word
    # for _ in len(range(word))
    # guess another letter
# else
    # post = "|"
    # bar = "___"    
    # head = "0"
    # left = "/"    
    # right = "\"


# print bar
# print post + "  " + post
# print "   " + head
# print "  " + left + post + right
# print "  " + left + post + right
# 



'''
____
|  |
   o
  /|\
  /|\
      
  '''
   

start = input("Welcome, Do you want to play the hangman game? (Y/N): ").lower()
if start == "y":
    word = random.choice(["oloche", "gold", "almond", "oche", "comfort", "aboje"])        
    missed = 0
    right = 0
    guessed_words = word[:]
    counter = 0
    hang_man = ["___", "|", "0", "/", "|", r"\\"]
    while  len(word) >= 1:
        guess = input("guess a letter in word: ").lower()        
        if guess in word:
            right += 1
            matched = word.index(guess)
            new_word = word[:matched] + word[matched+1:]
            word = new_word[:]            
            print("Good guess!")
            if len(word) == 0:
                print("YOU WON!!!")
                break
        else:
            missed += 1
            if missed == 1:
                print("___")
            elif missed == 2:
                print("___")
                print("|")
            elif missed == 3:
                print("____")
                print("|", end="")
                print("  |")
            elif missed == 4:
                print("____")
                print("|", end="")
                print("  |")
                print("   0")
            elif missed == 5:
                print("____")
                print("|", end="")
                print("  |")
                print("   0")  
                print("  /")              
            elif missed == 6:
                print("____")
                print("|", end="")
                print("  |")
                print("   0")
                print("  /", end="")
                print("|")
            elif missed == 7:
                print("____")
                print("|", end="")
                print("  |")
                print("   0")
                print("  /", end="")
                print("|", end="")
                print("\\")
            elif missed == 8:
                print("____")
                print("|", end="")
                print("  |")
                print("   0")
                print("  /", end="")
                print("|", end="")
                print("\\")
                print("  /")
            elif missed == 9:
                print()
                print("YOU LOST!!!")            
                print("____")
                print("|", end="")
                print("  |")
                print("   0")
                print("  /", end="")
                print("|", end="")
                print("\\")
                print("  /", end="")
                print(" \\")
                break  
            
         
                
            
    print("The correct word was", guessed_words)


