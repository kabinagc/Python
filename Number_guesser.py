# # method 1
# import random
# r = random.randrange(-1, 10)
# #  the 10 number is not generated its the upperbound
# print(r)

# guessing
import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a number larger than 0 next time.')
        quit()
else:
    print('please type a valid number next time')
    quit()
    
random_number = random.randint(0, top_of_range)

guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a Guess")
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print('Please type a number next time')
        continue
    if user_guess == random_number:
        print("you got it right")
        break
    else:
        if user_guess > random_number:
            print("you were above the number")
        else:
            print("You were below the number")

print("you got it in", guesses, "guesses")

