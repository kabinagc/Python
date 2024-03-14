name =input("Type your name:")
print("Welcome", name, "to this adventure")

answer = input(
    "You are on dirt road, it has come to and end. you can go left and right.Which way do you wanna go")

if answer == "left":
    answer = input("You have come to the river, you can walk around or you can swim accross")

    if answer == "swim":
        print("Ops there is an crocrodile in the river and you have been eaten by the crocrodile while swimming. Sorry")
    elif answer =="walk": 
        print("your decision was lucky enough for you because there were crocodiles in the river. Congratulations")
        answer = input("You cross th bridge and meet a stranger. Did you talk to them")

        if answer == "yes":
            print("you talk to the stranger and they give you gold. You WIN. Hurey")
        elif answer == "no":
            print("you ignore the stranger and they are offended and you lose")
        else:
            print("Not a valid option. You lose")
    else:
        print('Not a vaild option. You lose')

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross or go back?")

    if answer == "back":
        print("You walked for a miles, ran out of water and lost the game")
    elif answer == "cross":
        print("The bridge fell off and you were eaten by an crocrodile")
    else:
        print('Not a valid option. You loose')
else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)