import random
from colorama import Fore
import os

os.system('clear')
print ("We are playing Hangman.")

def get_dict():
   with open("/usr/share/dict/words", 'r') as file:
      dict = file.read()
   dict_list = []
   dict_list = dict.split()
   dict_5 = []
   for s in dict_list:
      if len(s)==5:
         dict_5.append(s)
   return(dict_5)


if __name__ == '__main__':
    print("If you want to play a 2 player game then enter the number 2")
    print("If you want to play a 1 player game then enter the number 1")
    secret=""
    choice=int(input())
    while  True:
       if choice==1:
          wordle_dict = get_dict()
          random_number = random.randint(0, len(wordle_dict)-1)
          secret = (wordle_dict[random_number]).lower()
          print("Lets start guessing! Good Luck! ")
          break
       elif choice==2:
          print("Player one will be entering the word for player to to guess")
          print("Player 1 please enter a word from the dictionary that is 5 letters")
          secret = input().lower()
          os.system('clear')
          break
           

    test_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
   
    # assign secret to the newly picked random word.
    
    secret_2=list(secret)
    secret_list = ["_"] * len(secret)
    print(secret_list)  
   
    chances = 6
    while (chances > 0):
        guess=input().lower()
   
        # Is guess a real word?
        if (guess not in test_list or (len(guess))>1):
            print(guess + " is not a valid word. Try doesnt count")
            continue
      
        guess_output = guess
        i = 0
        guess_correct = False
        for i in range(len(secret)):
            if (guess == secret[i]): # is character in secret?
                secret_2.remove(guess)
                secret_list[i]=guess
                guess_correct = True
            

        print(secret_list)

        if len(secret_2) == 0:
            print("You win!!!!")
            print("Game over!")
            exit

        if guess_correct == False:
            chances = chances - 1 # same as chances--    


        if (chances == 5):
            print (f"{Fore.LIGHTCYAN_EX}" + "0" + f"{Fore.RESET}")
        elif (chances == 4):
            print (f"{Fore.LIGHTCYAN_EX}" + "0" )
            print ( "|" + f"{Fore.RESET}")

        elif (chances == 3):
            print (f"{Fore.LIGHTCYAN_EX}" + " 0")
            print ( "\|" + f"{Fore.RESET}")

        elif (chances == 2):
            print (f"{Fore.LIGHTCYAN_EX}" + " 0")
            print ("\|/"  + f"{Fore.RESET}")
        elif (chances == 1):
            print (f"{Fore.LIGHTCYAN_EX}" + " 0")
            print ("\|/")
            print("/"   + f"{Fore.RESET}")
    

    print(f"{Fore.LIGHTCYAN_EX}" + " 0")
    print("\|/")
    print("/ \ " + f"{Fore.RESET}")
    print("You Lost :( Secret was : " + secret)

    print("Game over!")
