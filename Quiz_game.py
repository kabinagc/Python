print("Welcome to my computer guiz||")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input(" What does the RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input(" What does the CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input(" What does the GUI stand for? ")

# using "correct_answer" as a variable to store ans
correct_answer = "graphical user interface"
if answer.lower() == correct_answer:
    print('Correct!')
    score +=1
else:
    print('Incorrect!')
    print('The correct answer is:', correct_answer)
answer = input(" What does the Saas stand for? ")

if answer.lower() == "software as a service":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct! and your percentage is " + str((score/4*100)) + "%")
