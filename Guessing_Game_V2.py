''' Author : Saurav Ranjan Maharana
    Date : 14th November, 2019
    Purpose : Learning Py!
    Contact : saurav.maharana07@gmail.com
    Title :  Guessing Game!
    Computer's guess : 6
    User's Guess : 4
    print("Too Low")
    input_status = int(input("Guess the number again : "))
    User Guess : 7
    print("Too High")
    input_status = int(input("Guess the number again : "))
    User Guess : 6
    print("You Won!")
    print("Do you want to play again? Y/N)'''

import random
random_number = random.randint(1,10)
input_num = int(input("Guess a number : "))
while input_num != random_number:
    if input_num > random_number:
        print("Too High")
        input_num = int(input("Guess another number : "))
    else:
        print("Too Low")
        input_num = int(input("Guess another number : "))
print("You Won!")
# print("Computer's Input is : ", random_number)
# print("User's Input is : ", input_num)
play_again = str(input("Do You want to play more?(Y/N) "))
while play_again[0] == "Y" or play_again[0] == "y":
    import random
    random_number = random.randint(1,10)
    input_num = int(input("Guess a number : "))
    while input_num != random_number:
        if input_num > random_number:
            print("Too High")
            input_num = int(input("Guess another number : "))
        else:
            print("Too Low")
            input_num = int(input("Guess another number : "))
    print("You Won!")
    play_again = str(input("Do You want to play more?(Y/N) "))
    if play_again[0] == "N" or play_again[0] == "n":
        print("Thanks for playing! :)")

#When N, plays more
