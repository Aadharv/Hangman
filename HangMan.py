from multiprocessing.connection import wait
import random
name =input("What is your name?")
turns=12
wait
print("Okay! Good luck ", name)
words =["flower","moniter","imagination","perspective","preposition",'population','fracture','damaged','quarintined','awesomely','animated','demolishing','guarding','shreik','firefighter']
word = random.choice(words)

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print ("you win ,congratulations!")
        print("The word is :", word)
        break
    guess = input("guess a character: ")

    guesses += guess
    
    if guess not in word:
     turns -= 1
     print("wrong")
     print("You have,"+ turns, "more guesses")
     if turns == 0:
        print("you lose, better luck next time")

