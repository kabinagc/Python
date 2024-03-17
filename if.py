num = input("enter a number: ")

print(type(num))
num = int(num)

if num > 0:

    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")