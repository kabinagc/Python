first = float(input("enter first number =>"))
sec = float(input("enter second number =>"))
opr = str(input("enter Operation(+,-,*,/) =>"))

if opr == "+":
    total = first + sec
elif opr =="-":
    total = first - sec
elif opr =="*":
    total = first * sec
elif opr =="/":
    total = first / sec
else:
    total = str("please enter a valid operation ")

print (total)