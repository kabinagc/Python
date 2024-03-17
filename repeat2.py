x = "we live in kathmandu"
y = str(input("enter a letter to see whether it is repeated:"))

count = 0

for c in x:
    if c ==y or c == y.upper():
        count += 1
print(y, "is repeated", count ,"times")